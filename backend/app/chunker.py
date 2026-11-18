"""
chunker.py — Semantic-aware text chunking.

Splits LangChain Documents into overlapping chunks using
RecursiveCharacterTextSplitter, preserving Markdown structure.
"""
from __future__ import annotations

import logging
from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)


def chunk_documents(
    documents: List[Document],
    chunk_size: int = 512,
    chunk_overlap: int = 64,
) -> List[Document]:
    """
    Split documents into overlapping text chunks.

    Args:
        documents: Raw documents from the parser.
        chunk_size: Maximum characters per chunk.
        chunk_overlap: Overlap between consecutive chunks.

    Returns:
        List of chunked Document objects with enriched metadata.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n## ", "\n### ", "\n#### ", "\n", " ", ""],
        keep_separator=True,
        is_separator_regex=False,
    )

    chunks = splitter.split_documents(documents)

    # Enrich metadata with sequential chunk index
    for idx, chunk in enumerate(chunks):
        chunk.metadata["chunk_index"] = idx

    logger.info(
        "Chunked %d document(s) into %d chunks (size=%d, overlap=%d)",
        len(documents),
        len(chunks),
        chunk_size,
        chunk_overlap,
    )
    return chunks
