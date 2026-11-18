"""
retriever.py — Hybrid dense + sparse retrieval over the vector store.

Architecture:
  1. Dense retrieval  : ChromaDB + sentence-transformers embeddings.
  2. Sparse retrieval : BM25 (rank_bm25) over the same corpus.
  3. Fusion          : Reciprocal Rank Fusion (RRF) to merge ranked lists.
"""
from __future__ import annotations

import logging
import math
from dataclasses import dataclass, field
from typing import List, Optional

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from rank_bm25 import BM25Okapi  # type: ignore

logger = logging.getLogger(__name__)


@dataclass
class RetrievalResult:
    document: Document
    dense_rank: int = 0
    sparse_rank: int = 0
    rrf_score: float = 0.0


def _rrf_score(dense_rank: int, sparse_rank: int, k: int = 60) -> float:
    """Reciprocal Rank Fusion score."""
    score = 0.0
    if dense_rank > 0:
        score += 1.0 / (k + dense_rank)
    if sparse_rank > 0:
        score += 1.0 / (k + sparse_rank)
    return score


class HybridRetriever:
    """Combines ChromaDB (dense) and BM25 (sparse) with RRF fusion."""

    def __init__(
        self,
        persist_dir: str,
        collection_name: str,
        embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
        top_k: int = 10,
    ) -> None:
        self._top_k = top_k
        self._embedding_model_name = embedding_model

        logger.info("Loading embedding model: %s", embedding_model)
        self._embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

        self._vector_store = Chroma(
            collection_name=collection_name,
            persist_directory=persist_dir,
            embedding_function=self._embeddings,
        )

        # BM25 corpus is lazily built on first retrieve
        self._corpus: List[Document] = []
        self._bm25: Optional[BM25Okapi] = None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def document_count(self) -> int:
        try:
            return self._vector_store._collection.count()  # noqa: SLF001
        except Exception:
            return 0

    def get_vector_store(self) -> Chroma:
        return self._vector_store

    def build_bm25_index(self, documents: List[Document]) -> None:
        """Build (or rebuild) the in-memory BM25 index from a list of Documents."""
        self._corpus = documents
        tokenized = [doc.page_content.lower().split() for doc in documents]
        self._bm25 = BM25Okapi(tokenized)
        logger.info("BM25 index built with %d documents.", len(documents))

    def retrieve(self, query: str, top_k: Optional[int] = None) -> List[Document]:
        """
        Hybrid retrieve using dense + sparse + RRF.

        Args:
            query: Natural language query.
            top_k: Number of results to return (defaults to self._top_k).

        Returns:
            Ranked list of Documents.
        """
        k = top_k or self._top_k

        # 1. Dense retrieval
        dense_docs = self._dense_retrieve(query, k)

        # 2. Sparse retrieval (BM25)
        sparse_docs = self._sparse_retrieve(query, k)

        # 3. RRF fusion
        fused = self._fuse_rrf(dense_docs, sparse_docs)

        # Return top-k after fusion
        return [r.document for r in fused[:k]]

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _dense_retrieve(self, query: str, k: int) -> List[Document]:
        try:
            results = self._vector_store.similarity_search(query, k=k)
            logger.debug("Dense retrieval returned %d docs.", len(results))
            return results
        except Exception as exc:
            logger.warning("Dense retrieval failed: %s", exc)
            return []

    def _sparse_retrieve(self, query: str, k: int) -> List[Document]:
        if self._bm25 is None or not self._corpus:
            logger.debug("BM25 index not built; skipping sparse retrieval.")
            return []
        tokens = query.lower().split()
        scores = self._bm25.get_scores(tokens)
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        return [self._corpus[i] for i in top_indices if scores[i] > 0]

    def _fuse_rrf(self, dense: List[Document], sparse: List[Document]) -> List[RetrievalResult]:
        """Merge two ranked lists via Reciprocal Rank Fusion."""
        # Map content hash to result object
        results: dict[str, RetrievalResult] = {}

        for rank, doc in enumerate(dense, start=1):
            key = doc.page_content[:200]
            if key not in results:
                results[key] = RetrievalResult(document=doc)
            results[key].dense_rank = rank

        for rank, doc in enumerate(sparse, start=1):
            key = doc.page_content[:200]
            if key not in results:
                results[key] = RetrievalResult(document=doc)
            results[key].sparse_rank = rank

        for r in results.values():
            r.rrf_score = _rrf_score(r.dense_rank, r.sparse_rank)

        return sorted(results.values(), key=lambda r: r.rrf_score, reverse=True)
