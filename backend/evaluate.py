"""
evaluate.py — Standalone RAGAS benchmark runner for AutoDiag-RAG.

Usage:
    python evaluate.py [--questions-file PATH] [--output-file PATH] [--top-k N] [--top-n N]

Requires:
    - A running ChromaDB collection (pipeline must have been initialised/ingested).
    - GROQ_API_KEY and optionally OPENAI_API_KEY in .env.

This script:
  1. Loads evaluation Q&A pairs from a JSON file (or uses built-in sample questions).
  2. Runs each question through the AutoDiagPipeline.
  3. Evaluates answers with RAGAS metrics:
       - faithfulness        : Is the answer grounded in the context?
       - answer_relevancy    : How relevant is the answer to the question?
       - context_recall      : Does retrieved context cover the expected answer?
       - context_precision   : Is retrieved context concise and relevant?
  4. Prints a formatted results table and saves results to JSON.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

# Ensure the backend directory is on the path
sys.path.insert(0, str(Path(__file__).parent))

from app.config import get_settings
from app.pipeline import AutoDiagPipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("autodiag.evaluate")

# ---------------------------------------------------------------------------
# Built-in sample evaluation questions (Royal Enfield Hunter 350)
# ---------------------------------------------------------------------------
SAMPLE_QUESTIONS: List[Dict[str, str]] = [
    {
        "question": "What are the possible causes for a Royal Enfield Hunter 350 engine that cranks but will not start?",
        "ground_truth": "Possible causes include no fuel reaching the injector, a faulty fuel pump, a fouled spark plug, low compression, a defective crankshaft position sensor, or ECU faults.",
    },
    {
        "question": "What is the minimum brake pad thickness for the Hunter 350 front brakes?",
        "ground_truth": "The minimum front brake pad thickness is 1.5 mm. Pads below this measurement must be replaced immediately.",
    },
    {
        "question": "How do I diagnose excessive black smoke from the exhaust on the Hunter 350?",
        "ground_truth": "Black smoke indicates a rich fuel mixture. Check for a clogged air filter, faulty fuel injector (stuck open), incorrect throttle position sensor reading, or a failed lambda/O2 sensor.",
    },
    {
        "question": "What is the torque specification for the Hunter 350 cylinder head bolts?",
        "ground_truth": "Cylinder head bolts should be torqued to 25 Nm in a cross pattern, then re-torqued to 35 Nm after a heat cycle.",
    },
    {
        "question": "How do you reset ABS fault codes on the Royal Enfield Hunter 350?",
        "ground_truth": "To reset ABS fault codes, connect the RE diagnostic tool, navigate to ABS module, clear DTCs, then perform a 30 km/h test ride to verify the sensor wheel and wheel speed sensors.",
    },
    {
        "question": "What is the correct procedure for adjusting the clutch cable on the Hunter 350?",
        "ground_truth": "Loosen the lock nut at the handlebar adjuster, turn the barrel adjuster to achieve 10-15 mm of free play at the lever, then tighten the lock nut. Fine-tune at the engine-side adjuster if needed.",
    },
    {
        "question": "What does DTC P0335 indicate on the Hunter 350?",
        "ground_truth": "DTC P0335 indicates a Crankshaft Position Sensor (CKP) circuit malfunction. Check the sensor gap, wiring harness continuity, and sensor output voltage.",
    },
    {
        "question": "When should the engine oil be changed on a new Royal Enfield Hunter 350?",
        "ground_truth": "Engine oil should be changed at the 500 km break-in service, then every 3,000 km or 6 months thereafter, whichever comes first.",
    },
]


# ---------------------------------------------------------------------------
# RAGAS evaluation
# ---------------------------------------------------------------------------

def run_ragas_evaluation(
    questions: List[Dict[str, str]],
    pipeline: AutoDiagPipeline,
    top_k: int = 10,
    top_n: int = 4,
) -> Dict[str, Any]:
    """
    Run RAGAS evaluation over a list of Q&A pairs.

    Returns:
        dict with 'metrics' (averages) and 'per_question' (detailed rows).
    """
    logger.info("Running %d questions through RAG pipeline...", len(questions))

    # Collect pipeline outputs
    queries: List[str] = []
    answers: List[str] = []
    contexts: List[List[str]] = []
    ground_truths: List[str] = []

    for i, qa in enumerate(questions, start=1):
        q = qa["question"]
        gt = qa.get("ground_truth", "")
        logger.info("[%d/%d] Querying: %s", i, len(questions), q[:80])

        try:
            result = pipeline.run(query=q, top_k=top_k, top_n=top_n)
            ctx = [r.document.page_content for r in result.sources]
        except Exception as exc:
            logger.error("Pipeline error for question %d: %s", i, exc)
            result = None
            ctx = []

        queries.append(q)
        answers.append(result.answer if result else "[PIPELINE ERROR]")
        contexts.append(ctx)
        ground_truths.append(gt)

    # RAGAS evaluation
    try:
        from datasets import Dataset  # type: ignore
        from ragas import evaluate  # type: ignore
        from ragas.metrics import (
            answer_relevancy,  # type: ignore
            context_precision,  # type: ignore
            context_recall,  # type: ignore
            faithfulness,  # type: ignore
        )

        dataset = Dataset.from_dict({
            "question": queries,
            "answer": answers,
            "contexts": contexts,
            "ground_truth": ground_truths,
        })

        logger.info("Starting RAGAS evaluation (this may take a few minutes)...")
        result_df = evaluate(
            dataset,
            metrics=[
                faithfulness,
                answer_relevancy,
                context_recall,
                context_precision,
            ],
        )

        metrics = result_df.to_pandas().mean(numeric_only=True).to_dict()
        per_q = result_df.to_pandas().to_dict(orient="records")

    except ImportError as exc:
        logger.warning("RAGAS or datasets not available: %s. Computing basic stats only.", exc)
        metrics = {"note": "RAGAS not available; install ragas and datasets"}
        per_q = [
            {"question": q, "answer": a, "num_context_chunks": len(c)}
            for q, a, c in zip(queries, answers, contexts)
        ]

    return {
        "num_questions": len(questions),
        "metrics": metrics,
        "per_question": per_q,
        "raw": {
            "queries": queries,
            "answers": answers,
            "contexts": contexts,
            "ground_truths": ground_truths,
        },
    }


def print_results(results: Dict[str, Any]) -> None:
    """Pretty-print evaluation results to stdout."""
    print("\n" + "=" * 70)
    print("  AutoDiag-RAG  \u2014  RAGAS Evaluation Results")
    print("=" * 70)
    print(f"  Questions evaluated : {results['num_questions']}")
    print()
    print("  AGGREGATE METRICS")
    print("  " + "-" * 40)
    for k, v in results["metrics"].items():
        if isinstance(v, float):
            print(f"  {k:<30} {v:.4f}")
        else:
            print(f"  {k:<30} {v}")
    print()
    print("  PER-QUESTION SUMMARY")
    print("  " + "-" * 40)
    for i, row in enumerate(results["per_question"], start=1):
        q = results["raw"]["queries"][i - 1][:60]
        a = results["raw"]["answers"][i - 1][:80]
        print(f"  [{i}] Q: {q}")
        print(f"       A: {a}")
        for metric in ["faithfulness", "answer_relevancy", "context_recall", "context_precision"]:
            if metric in row:
                print(f"       {metric}: {row[metric]:.4f}")
        print()
    print("=" * 70)


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run RAGAS evaluation on AutoDiag-RAG.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--questions-file",
        type=str,
        default=None,
        help="Path to JSON file with evaluation Q&A pairs [{question, ground_truth}, ...]",
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default="eval_results.json",
        help="Path to save evaluation results JSON.",
    )
    parser.add_argument("--top-k", type=int, default=10, help="Retriever top-k.")
    parser.add_argument("--top-n", type=int, default=4, help="Reranker top-n.")
    args = parser.parse_args()

    # Load questions
    if args.questions_file:
        qfile = Path(args.questions_file)
        if not qfile.exists():
            logger.error("Questions file not found: %s", qfile)
            sys.exit(1)
        questions = json.loads(qfile.read_text(encoding="utf-8"))
        logger.info("Loaded %d questions from %s", len(questions), qfile)
    else:
        questions = SAMPLE_QUESTIONS
        logger.info("Using %d built-in sample questions.", len(questions))

    # Initialise pipeline
    settings = get_settings()
    pipeline = AutoDiagPipeline(settings)
    pipeline.initialise()

    if pipeline.document_count == 0:
        logger.error(
            "Vector store is empty. Please run the API server first to auto-ingest "
            "sample_manual.md, or POST to /ingest."
        )
        sys.exit(1)

    # Run evaluation
    start = time.perf_counter()
    results = run_ragas_evaluation(
        questions,
        pipeline,
        top_k=args.top_k,
        top_n=args.top_n,
    )
    elapsed = time.perf_counter() - start
    results["elapsed_seconds"] = round(elapsed, 2)

    # Print
    print_results(results)

    # Save
    output = Path(args.output_file)
    # Remove raw large data before saving to keep file manageable
    save_results = {k: v for k, v in results.items() if k != "raw"}
    output.write_text(json.dumps(save_results, indent=2, default=str), encoding="utf-8")
    logger.info("Results saved to %s", output.resolve())


if __name__ == "__main__":
    main()
