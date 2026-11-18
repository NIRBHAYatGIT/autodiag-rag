"""
parser.py — Document ingestion layer.

Supports:
  • Markdown files  → parsed directly.
  • Plain text files → parsed directly.
  • PDF files       → parsed locally via pypdf, or via LlamaParse if API key provided.
Returns a list of LangChain Document objects.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import List

from langchain_core.documents import Document

logger = logging.getLogger(__name__)


def _parse_markdown(file_path: Path) -> List[Document]:
    """Read a Markdown or text file and return a single Document."""
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    return [
        Document(
            page_content=text,
            metadata={"source": file_path.name, "file_type": file_path.suffix.lower()},
        )
    ]


def _parse_pdf_pypdf(file_path: Path) -> List[Document]:
    """Parse a PDF locally using pypdf (offline, no API key needed)."""
    import pypdf

    reader = pypdf.PdfReader(str(file_path))
    documents: List[Document] = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        if text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": file_path.name,
                        "file_type": "pdf",
                        "page": i + 1,
                    },
                )
            )
    logger.info("pypdf extracted %d pages from %s", len(documents), file_path.name)
    return documents


def _parse_pdf_llamaparse(file_path: Path, api_key: str) -> List[Document]:
    """Parse a PDF using LlamaParse and return Documents."""
    try:
        from llama_parse import LlamaParse  # type: ignore
    except ImportError as e:
        logger.warning("llama-parse not available, falling back to local pypdf: %s", e)
        return _parse_pdf_pypdf(file_path)

    parser = LlamaParse(
        api_key=api_key,
        result_type="markdown",
        verbose=False,
    )
    llama_docs = parser.load_data(str(file_path))
    documents: List[Document] = []
    for i, doc in enumerate(llama_docs):
        documents.append(
            Document(
                page_content=doc.text,
                metadata={
                    "source": file_path.name,
                    "file_type": "pdf",
                    "page": i + 1,
                },
            )
        )
    logger.info("LlamaParse produced %d pages from %s", len(documents), file_path.name)
    return documents


def parse_document(file_path: str | Path, llama_api_key: str = "") -> List[Document]:
    """
    Parse a document file and return a list of LangChain Documents.

    Args:
        file_path: Path to the file (Markdown, text, or PDF).
        llama_api_key: Optional LlamaCloud API key for advanced cloud PDF parsing.

    Returns:
        List of Document objects ready for chunking.

    Raises:
        ValueError: If the file type is unsupported.
        FileNotFoundError: If the file does not exist.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    suffix = path.suffix.lower()
    logger.info("Parsing %s (type=%s)", path.name, suffix)

    if suffix in (".md", ".markdown", ".txt"):
        return _parse_markdown(path)
    elif suffix == ".pdf":
        if llama_api_key:
            return _parse_pdf_llamaparse(path, llama_api_key)
        else:
            return _parse_pdf_pypdf(path)
    else:
        raise ValueError(f"Unsupported file type: {suffix!r}. Supported: .md, .markdown, .txt, .pdf")
