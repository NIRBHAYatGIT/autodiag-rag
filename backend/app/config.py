"""Centralised settings – loaded once from .env via pydantic-settings."""
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # LLM
    groq_api_key: str = ""
    llm_model: str = "openai/gpt-oss-120b"
    llm_max_tokens: int = 1024
    llm_temperature: float = 0.2

    # LlamaParse
    llama_cloud_api_key: str = ""

    # ChromaDB
    chroma_persist_dir: str = "./chroma_db"
    chroma_collection: str = "autodiag_manual"

    # Embedding
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Retrieval
    retriever_top_k: int = 10
    bm25_top_k: int = 10
    reranker_top_n: int = 4

    # Chunking
    chunk_size: int = 512
    chunk_overlap: int = 64

    # Evaluation
    openai_api_key: str = ""


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached singleton Settings instance."""
    return Settings()
