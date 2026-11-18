"""Pydantic v2 request/response schemas for AutoDiag-RAG."""
from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field


# ── Ingest ────────────────────────────────────────────────────────────────────

class IngestRequest(BaseModel):
    """Body for the /ingest endpoint when uploading via JSON (path-based)."""
    file_path: str = Field(..., description="Absolute or relative path to the manual file (PDF or Markdown).")
    force_reindex: bool = Field(False, description="Drop existing collection and re-ingest from scratch.")


class IngestResponse(BaseModel):
    status: str
    chunks_indexed: int
    collection: str
    message: str


# ── Diagnose ──────────────────────────────────────────────────────────────────

class DiagnoseRequest(BaseModel):
    query: str = Field(..., min_length=5, description="Natural-language diagnostic question.")
    top_k: Optional[int] = Field(None, ge=1, le=20, description="Override default retriever top-k.")
    top_n: Optional[int] = Field(None, ge=1, le=10, description="Override default reranker top-n.")


class SourceChunk(BaseModel):
    content: str
    source: str
    chunk_index: int
    score: float


class DiagnoseResponse(BaseModel):
    query: str
    answer: str
    sources: List[SourceChunk]
    model: str
    retrieval_ms: float
    generation_ms: float
    total_ms: float


# ── Health ────────────────────────────────────────────────────────────────────

class HealthResponse(BaseModel):
    status: str
    vector_store_ready: bool
    documents_indexed: int
    llm_model: str
    embedding_model: str
