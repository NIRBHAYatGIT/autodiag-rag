"""
main.py — AutoDiag-RAG FastAPI Application.

Endpoints:
  GET  /health           — Health check with vector store status.
  POST /ingest           — Ingest a document by file path.
  POST /ingest/upload    — Ingest an uploaded file (multipart/form-data).
  POST /diagnose         — Run RAG pipeline on a diagnostic question.

On startup the app auto-indexes backend/sample_manual.md if the vector
store is empty, giving a zero-config demo experience.
"""
from __future__ import annotations

import logging
import os
import threading
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Annotated

import uvicorn
from fastapi import FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from app.config import get_settings
from app.pipeline import AutoDiagPipeline
from app.schemas import (
    DiagnoseRequest,
    DiagnoseResponse,
    HealthResponse,
    IngestRequest,
    IngestResponse,
)

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
logger = logging.getLogger("autodiag.main")

# ---------------------------------------------------------------------------
# Application state
# ---------------------------------------------------------------------------
_pipeline: AutoDiagPipeline | None = None
_init_thread: threading.Thread | None = None


def _bg_initialize(pipeline: AutoDiagPipeline, sample_path: Path) -> None:
    """Run model loading and initial indexing in a background thread."""
    try:
        logger.info("Background initialization started: loading models and vector store...")
        pipeline.initialise()

        # Auto-index sample manual if collection is empty
        if pipeline.document_count == 0 and sample_path.exists():
            logger.info("Vector store empty — auto-indexing %s", sample_path.name)
            try:
                n = pipeline.ingest(sample_path)
                logger.info("Auto-indexed %d chunks from %s", n, sample_path.name)
            except Exception as exc:
                logger.error("Auto-index failed: %s", exc)
        else:
            logger.info("Vector store has %d documents. Skipping auto-index.", pipeline.document_count)

        logger.info("=== AutoDiag-RAG background initialization complete ===")
    except Exception as exc:
        logger.exception("Background initialization error: %s", exc)


def get_pipeline() -> AutoDiagPipeline:
    global _pipeline, _init_thread
    if _pipeline is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Pipeline is not created.",
        )
    if not _pipeline.is_ready:
        if _init_thread and _init_thread.is_alive():
            _init_thread.join(timeout=20)
        if not _pipeline.is_ready:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Knowledge base is still loading into memory. Please retry in a few seconds.",
            )
    return _pipeline


# ---------------------------------------------------------------------------
# Lifespan: startup / shutdown
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    global _pipeline, _init_thread
    settings = get_settings()
    logger.info("=== AutoDiag-RAG starting up (fast port bind) ===")

    _pipeline = AutoDiagPipeline(settings)
    sample_path = Path(__file__).parent / "sample_manual.md"

    # Start heavy initialization in background so Uvicorn binds port instantly!
    _init_thread = threading.Thread(
        target=_bg_initialize,
        args=(_pipeline, sample_path),
        daemon=True,
    )
    _init_thread.start()

    logger.info("=== Port open and accepting connections ===")
    yield

    logger.info("=== AutoDiag-RAG shutting down ===")


# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------
app = FastAPI(
    title="AutoDiag-RAG",
    description="Production-grade Retrieval-Augmented Generation system for vehicle diagnostics.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/", tags=["UI"])
async def root():
    """Serve the Web Terminal UI directly with no-cache headers."""
    html_file = Path(__file__).resolve().parent.parent / "frontend" / "index.html"
    return FileResponse(
        html_file,
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
        },
    )


@app.get("/health", response_model=HealthResponse, tags=["System"])
async def health() -> HealthResponse:
    """Return service health status and vector store statistics."""
    settings = get_settings()
    ready = _pipeline is not None and _pipeline.is_ready
    count = _pipeline.document_count if ready else 0
    return HealthResponse(
        status="ok" if ready else "initialising",
        vector_store_ready=ready,
        documents_indexed=count,
        llm_model=settings.llm_model,
        embedding_model=settings.embedding_model,
    )


@app.post("/ingest", response_model=IngestResponse, tags=["Ingestion"])
async def ingest(body: IngestRequest) -> IngestResponse:
    """
    Ingest a document by providing its file-system path.

    Use this endpoint for server-side files or automated pipelines.
    For browser uploads, use POST /ingest/upload.
    """
    pipeline = get_pipeline()
    try:
        n = pipeline.ingest(body.file_path, force_reindex=body.force_reindex)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception("Ingest failed for %s", body.file_path)
        raise HTTPException(status_code=500, detail=f"Ingest error: {exc}") from exc

    settings = get_settings()
    return IngestResponse(
        status="success",
        chunks_indexed=n,
        collection=settings.chroma_collection,
        message=f"Successfully indexed {n} chunks from {body.file_path}.",
    )


@app.post("/ingest/upload", response_model=IngestResponse, tags=["Ingestion"])
async def ingest_upload(
    file: Annotated[UploadFile, File(description="Manual file (.md or .pdf)")],
    force_reindex: Annotated[bool, Form()] = False,
) -> IngestResponse:
    """
    Ingest an uploaded manual file.

    Accepts multipart/form-data with a file field.
    Temporary file is deleted after indexing.
    """
    import tempfile
    import shutil

    pipeline = get_pipeline()
    settings = get_settings()

    orig_name = Path(file.filename or "uploaded_manual.md").name
    temp_dir = Path(tempfile.gettempdir()) / "autodiag_uploads"
    temp_dir.mkdir(parents=True, exist_ok=True)
    tmp_path = temp_dir / orig_name
    with open(tmp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        n = pipeline.ingest(tmp_path, force_reindex=force_reindex)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    finally:
        tmp_path.unlink(missing_ok=True)

    return IngestResponse(
        status="success",
        chunks_indexed=n,
        collection=settings.chroma_collection,
        message=f"Uploaded and indexed {n} chunks from {file.filename}.",
    )


@app.post("/diagnose", response_model=DiagnoseResponse, tags=["Diagnosis"])
async def diagnose(body: DiagnoseRequest) -> DiagnoseResponse:
    """
    Run the full RAG pipeline on a diagnostic question.

    Returns a grounded answer with source citations and latency metrics.
    """
    pipeline = get_pipeline()

    if pipeline.document_count == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No documents have been indexed yet. Please POST to /ingest first.",
        )

    try:
        result = pipeline.run(
            query=body.query,
            top_k=body.top_k,
            top_n=body.top_n,
        )
    except Exception as exc:
        logger.exception("Diagnosis failed for query: %s", body.query)
        raise HTTPException(status_code=500, detail=f"Pipeline error: {exc}") from exc

    return pipeline.to_diagnose_response(body.query, result)


# ---------------------------------------------------------------------------
# Dev entrypoint
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        log_level="info",
    )
