"""
reranker.py — Cross-encoder re-ranking with FlashRank.

Takes candidate documents from the hybrid retriever and re-ranks them
using a lightweight cross-encoder model for higher precision.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import List

from langchain_core.documents import Document

logger = logging.getLogger(__name__)


@dataclass
class RankedResult:
    document: Document
    score: float
    chunk_index: int


class FlashReranker:
    """Wraps FlashRank to re-score a list of candidate Documents."""

    def __init__(self, top_n: int = 4) -> None:
        self._top_n = top_n
        self._ranker = None  # Lazy init to avoid import-time overhead

    def _get_ranker(self):
        if self._ranker is None:
            try:
                from flashrank import Ranker  # type: ignore
                self._ranker = Ranker(model_name="ms-marco-MiniLM-L-12-v2", cache_dir="/tmp/flashrank")
            except Exception as exc:
                logger.warning("FlashRank unavailable (%s). Falling back to pass-through.", exc)
                self._ranker = False  # sentinel
        return self._ranker

    def rerank(self, query: str, documents: List[Document], top_n: int | None = None) -> List[RankedResult]:
        """
        Re-rank documents using FlashRank cross-encoder.

        Args:
            query: Original user query.
            documents: Candidate documents from the retriever.
            top_n: How many to return (defaults to self._top_n).

        Returns:
            Sorted list of RankedResult with scores.
        """
        n = top_n or self._top_n
        ranker = self._get_ranker()

        if not ranker:  # fallback: return documents as-is with dummy scores
            return [
                RankedResult(
                    document=doc,
                    score=1.0 - (i / max(len(documents), 1)),
                    chunk_index=doc.metadata.get("chunk_index", i),
                )
                for i, doc in enumerate(documents[:n])
            ]

        try:
            from flashrank import RerankRequest  # type: ignore

            passages = [
                {"id": i, "text": doc.page_content}
                for i, doc in enumerate(documents)
            ]
            request = RerankRequest(query=query, passages=passages)
            response = ranker.rerank(request)

            results: List[RankedResult] = []
            for item in response[:n]:
                doc = documents[item["id"]]
                results.append(
                    RankedResult(
                        document=doc,
                        score=float(item["score"]),
                        chunk_index=doc.metadata.get("chunk_index", item["id"]),
                    )
                )
            logger.info("Reranked %d candidates -> top %d", len(documents), len(results))
            return results

        except Exception as exc:
            logger.error("Reranking failed: %s. Returning unreranked.", exc)
            return [
                RankedResult(
                    document=doc,
                    score=1.0 - (i / max(len(documents), 1)),
                    chunk_index=doc.metadata.get("chunk_index", i),
                )
                for i, doc in enumerate(documents[:n])
            ]
