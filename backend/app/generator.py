"""
generator.py — LLM answer generation with citation grounding.

Uses Groq-hosted LLaMA models via langchain-groq.
Builds a structured RAG prompt that instructs the model to cite sources.
"""
from __future__ import annotations

import logging
import os
from typing import List, Optional

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from .reranker import RankedResult

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """\
You are AutoDiag, an expert automotive diagnostic assistant specialising in Royal Enfield motorcycles.
Your role is to help technicians and riders diagnose and resolve mechanical, electrical, and electronic faults.

GUIDELINES:
1. Answer ONLY based on the provided context chunks. Do not fabricate information.
2. If the context does not contain sufficient information, say so clearly.
3. Structure your answer with clear headings and numbered steps where appropriate.
4. Include specific values (torque specs, voltage thresholds, gap measurements) when present in the context.
5. Add a "CAUTION" note if any step involves safety risks.
6. At the end of your answer, list the source sections you relied on under a "Sources" heading.
"""


def _build_context_block(ranked_results: List[RankedResult]) -> str:
    """Format retrieved chunks into a numbered context block for the prompt."""
    blocks = []
    for i, result in enumerate(ranked_results, start=1):
        source = result.document.metadata.get("source", "Unknown")
        blocks.append(
            f"[CHUNK {i}] (source: {source}, score: {result.score:.4f})\n"
            f"{result.document.page_content}"
        )
    return "\n\n---\n\n".join(blocks)


def _build_user_message(query: str, context: str) -> str:
    return f"""CONTEXT:
{context}

---

DIAGNOSTIC QUESTION:
{query}

Provide a thorough, step-by-step diagnostic answer grounded in the context above."""


class DiagnosticGenerator:
    """Wraps a Groq LLM to generate grounded diagnostic answers."""

    def __init__(
        self,
        groq_api_key: str = "",
        model: str = "openai/gpt-oss-120b",
        max_tokens: int = 1024,
        temperature: float = 0.2,
    ) -> None:
        self._model_name = model
        self._api_key = groq_api_key or os.environ.get("GROQ_API_KEY", "")
        self._max_tokens = max_tokens
        self._temperature = temperature
        self._llm: Optional[ChatGroq] = None

        if self._api_key:
            try:
                self._llm = ChatGroq(
                    api_key=self._api_key,
                    model=model,
                    max_tokens=max_tokens,
                    temperature=temperature,
                )
                logger.info("DiagnosticGenerator initialised with model=%s", model)
            except Exception as e:
                logger.warning("ChatGroq immediate init skipped: %s", e)

    @property
    def model_name(self) -> str:
        return self._model_name

    def _get_llm(self) -> ChatGroq:
        if self._llm is None:
            key = self._api_key or os.environ.get("GROQ_API_KEY", "")
            if not key:
                raise ValueError(
                    "GROQ_API_KEY is not configured. Please set the GROQ_API_KEY environment variable."
                )
            self._llm = ChatGroq(
                api_key=key,
                model=self._model_name,
                max_tokens=self._max_tokens,
                temperature=self._temperature,
            )
        return self._llm

    def generate(
        self,
        query: str,
        ranked_results: List[RankedResult],
    ) -> str:
        """
        Generate a diagnostic answer from re-ranked context.

        Args:
            query: Original user diagnostic question.
            ranked_results: Re-ranked chunks from the reranker.

        Returns:
            Generated answer string.
        """
        if not ranked_results:
            return (
                "I could not find relevant information in the vehicle manual for your query. "
                "Please rephrase your question or check the manual index."
            )

        context = _build_context_block(ranked_results)
        user_msg = _build_user_message(query, context)

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_msg),
        ]

        logger.debug("Sending %d context chunks to LLM.", len(ranked_results))
        llm = self._get_llm()
        response = llm.invoke(messages)
        answer = response.content
        logger.info("LLM generated %d chars.", len(answer))
        return answer
