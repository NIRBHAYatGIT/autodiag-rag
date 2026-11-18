"""
pipeline.py — Orchestrates the full RAG pipeline.

Lifecycle:
  ingest() → parse → chunk → embed → store in ChromaDB + build BM25 index
  run()    → retrieve (hybrid RRF) → rerank (FlashRank) → generate (Groq LLM)
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from langchain_core.documents import Document

from .chunker import chunk_documents
from .config import Settings
from .generator import DiagnosticGenerator
from .parser import parse_document
from .reranker import FlashReranker, RankedResult
from .retriever import HybridRetriever
from .schemas import DiagnoseResponse, SourceChunk

logger = logging.getLogger(__name__)


@dataclass
class PipelineResult:
    answer: str
    sources: List[RankedResult]
    retrieval_ms: float
    generation_ms: float


class AutoDiagPipeline:
    """End-to-end RAG pipeline for vehicle diagnostics."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._retriever: Optional[HybridRetriever] = None
        self._reranker: Optional[FlashReranker] = None
        self._generator: Optional[DiagnosticGenerator] = None
        self._is_ready = False

    # ------------------------------------------------------------------
    # Initialisation
    # ------------------------------------------------------------------

    def initialise(self) -> None:
        """Lazily initialise all pipeline components."""
        s = self._settings

        self._retriever = HybridRetriever(
            persist_dir=s.chroma_persist_dir,
            collection_name=s.chroma_collection,
            embedding_model=s.embedding_model,
            top_k=s.retriever_top_k,
        )

        self._reranker = FlashReranker(top_n=s.reranker_top_n)

        self._generator = DiagnosticGenerator(
            groq_api_key=s.groq_api_key,
            model=s.llm_model,
            max_tokens=s.llm_max_tokens,
            temperature=s.llm_temperature,
        )

        # Rebuild BM25 index from existing vector store
        self._rebuild_bm25_from_store()
        self._is_ready = True
        logger.info("AutoDiagPipeline ready. Docs in store: %d", self._retriever.document_count)

    def _rebuild_bm25_from_store(self) -> None:
        """Load all stored chunks and build BM25 index."""
        try:
            store = self._retriever.get_vector_store()
            result = store._collection.get(include=["documents", "metadatas"])  # noqa: SLF001
            raw_docs = result.get("documents", [])
            metadatas = result.get("metadatas", [])
            if not raw_docs:
                logger.info("Vector store is empty; BM25 index will be built after ingest.")
                return
            documents = [
                Document(page_content=text, metadata=meta)
                for text, meta in zip(raw_docs, metadatas)
            ]
            self._retriever.build_bm25_index(documents)
        except Exception as exc:
            logger.warning("Could not rebuild BM25 from store: %s", exc)

    # ------------------------------------------------------------------
    # Ingest
    # ------------------------------------------------------------------

    def ingest(
        self,
        file_path: str | Path,
        force_reindex: bool = False,
    ) -> int:
        """
        Parse, chunk, embed, and store a document.

        Args:
            file_path: Path to the manual file.
            force_reindex: If True, clear the collection before ingesting.

        Returns:
            Number of chunks indexed.
        """
        if not self._is_ready:
            self.initialise()

        s = self._settings

        if force_reindex:
            logger.warning("force_reindex=True: dropping collection %s", s.chroma_collection)
            store = self._retriever.get_vector_store()
            store._client.delete_collection(s.chroma_collection)  # noqa: SLF001
            # Re-create retriever to get fresh collection
            self._retriever = HybridRetriever(
                persist_dir=s.chroma_persist_dir,
                collection_name=s.chroma_collection,
                embedding_model=s.embedding_model,
                top_k=s.retriever_top_k,
            )

        # Parse
        documents = parse_document(file_path, llama_api_key=s.llama_cloud_api_key)

        # Chunk
        chunks = chunk_documents(
            documents,
            chunk_size=s.chunk_size,
            chunk_overlap=s.chunk_overlap,
        )

        # Embed + store
        store = self._retriever.get_vector_store()
        texts = [c.page_content for c in chunks]
        metadatas = [c.metadata for c in chunks]
        store.add_texts(texts=texts, metadatas=metadatas)

        # Rebuild BM25 over the full collection
        self._rebuild_bm25_from_store()

        logger.info("Ingested %d chunks from %s", len(chunks), file_path)
        return len(chunks)

    # ------------------------------------------------------------------
    # Query
    # ------------------------------------------------------------------

    def run(
        self,
        query: str,
        top_k: Optional[int] = None,
        top_n: Optional[int] = None,
    ) -> PipelineResult:
        """
        Run the full RAG pipeline for a diagnostic query.

        Args:
            query: User's diagnostic question.
            top_k: Override retriever top-k.
            top_n: Override reranker top-n.

        Returns:
            PipelineResult with answer and provenance.
        """
        if not self._is_ready:
            self.initialise()

        # Retrieve
        t0 = time.perf_counter()
        candidates = self._retriever.retrieve(query, top_k=top_k)
        retrieval_ms = (time.perf_counter() - t0) * 1000

        # Rerank
        ranked = self._reranker.rerank(query, candidates, top_n=top_n)

        # Generate
        t1 = time.perf_counter()
        answer = self._generator.generate(query, ranked)
        generation_ms = (time.perf_counter() - t1) * 1000

        return PipelineResult(
            answer=answer,
            sources=ranked,
            retrieval_ms=retrieval_ms,
            generation_ms=generation_ms,
        )

    def to_diagnose_response(self, query: str, result: PipelineResult) -> DiagnoseResponse:
        """Convert a PipelineResult into the API response schema."""
        sources = [
            SourceChunk(
                content=r.document.page_content,
                source=r.document.metadata.get("source", "unknown"),
                chunk_index=r.chunk_index,
                score=round(r.score, 4),
            )
            for r in result.sources
        ]
        total_ms = result.retrieval_ms + result.generation_ms
        return DiagnoseResponse(
            query=query,
            answer=result.answer,
            sources=sources,
            model=self._generator.model_name,
            retrieval_ms=round(result.retrieval_ms, 2),
            generation_ms=round(result.generation_ms, 2),
            total_ms=round(total_ms, 2),
        )

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    @property
    def is_ready(self) -> bool:
        return self._is_ready

    @property
    def document_count(self) -> int:
        if self._retriever:
            return self._retriever.document_count
        return 0
