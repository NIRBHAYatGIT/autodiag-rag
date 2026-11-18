# AutoDiag-RAG

> Production-grade Retrieval-Augmented Generation system for vehicle diagnostics.
> Specialised for Royal Enfield motorcycles with a hybrid dense+sparse retrieval pipeline.

---

## Architecture

```
User Query
    │
    ▼
FastAPI /diagnose
    │
    ├── HybridRetriever ──► ChromaDB (dense, all-MiniLM-L6-v2 embeddings)
    │                  └──► BM25Okapi (sparse, in-memory)
    │                            │
    │                     RRF Fusion (Reciprocal Rank Fusion)
    │                            │
    ├── FlashReranker ──► ms-marco-MiniLM-L-12-v2 cross-encoder
    │
    └── DiagnosticGenerator ──► Groq LLaMA-3.1-8b-instant
                                        │
                                   Grounded Answer + Citations
```

## File Structure

```
autodiag-rag/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py        # Pydantic-settings (reads .env)
│   │   ├── schemas.py       # Request/response Pydantic v2 schemas
│   │   ├── parser.py        # Markdown / PDF (LlamaParse) ingestion
│   │   ├── chunker.py       # RecursiveCharacterTextSplitter
│   │   ├── retriever.py     # HybridRetriever (ChromaDB + BM25 + RRF)
│   │   ├── reranker.py      # FlashReranker (cross-encoder)
│   │   ├── generator.py     # DiagnosticGenerator (Groq LLM)
│   │   └── pipeline.py      # AutoDiagPipeline orchestrator
│   ├── main.py              # FastAPI application
│   ├── evaluate.py          # Standalone RAGAS benchmark runner
│   ├── sample_manual.md     # Royal Enfield Hunter 350 manual excerpt
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   └── index.html           # Single-file dark-mode diagnostic terminal UI
└── README.md
```

## Quick Start

### 1. Prerequisites

- Python 3.10+
- A [Groq API key](https://console.groq.com/) (free tier works)
- Optional: [LlamaCloud API key](https://cloud.llamaindex.ai/) for PDF parsing

### 2. Create & Activate Virtual Environment

```bash
cd autodiag-rag/backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note**: First install may take 2-5 minutes (downloading sentence-transformer models).

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env and set GROQ_API_KEY (minimum required)
```

### 5. Run the Backend

```bash
# From the backend/ directory
python main.py
```

Or with uvicorn directly:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

On first startup, the server will **automatically index** `sample_manual.md` into ChromaDB if the vector store is empty.

### 6. Open the Frontend

Open `frontend/index.html` directly in your browser (no server needed):

```bash
# Windows
start frontend\index.html

# macOS
open frontend/index.html
```

Or serve it with any static server:

```bash
python -m http.server 3000 --directory frontend
# Open http://localhost:3000
```

---

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Service health + vector store stats |
| `POST` | `/diagnose` | Run RAG diagnostic query |
| `POST` | `/ingest` | Index a server-side file by path |
| `POST` | `/ingest/upload` | Index an uploaded file (multipart) |

Interactive API docs: **http://localhost:8000/docs**

### Example: Diagnose

```bash
curl -X POST http://localhost:8000/diagnose \
  -H "Content-Type: application/json" \
  -d '{"query": "Engine cranks but will not start"}'
```

### Example: Ingest a custom PDF

```bash
curl -X POST http://localhost:8000/ingest/upload \
  -F "file=@/path/to/your_manual.pdf"
```

---

## Running the RAGAS Evaluation

```bash
cd backend

# Run with built-in 8 sample questions
python evaluate.py

# Run with your own questions file
python evaluate.py --questions-file my_questions.json --output-file results.json

# Custom retrieval parameters
python evaluate.py --top-k 15 --top-n 5
```

### Questions file format

```json
[
  {
    "question": "What causes black smoke from the exhaust?",
    "ground_truth": "Black smoke indicates a rich mixture..."
  }
]
```

---

## Key Configuration (`.env`)

| Variable | Default | Description |
|----------|---------|-------------|
| `GROQ_API_KEY` | *(required)* | Groq API key |
| `LLM_MODEL` | `llama-3.1-8b-instant` | Groq model name |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | HuggingFace embedding model |
| `RETRIEVER_TOP_K` | `10` | Chunks fetched per retriever |
| `RERANKER_TOP_N` | `4` | Chunks passed to LLM after reranking |
| `CHUNK_SIZE` | `512` | Characters per chunk |
| `CHUNK_OVERLAP` | `64` | Overlap between chunks |
| `CHROMA_PERSIST_DIR` | `./chroma_db` | ChromaDB storage path |
| `LLAMA_CLOUD_API_KEY` | *(optional)* | Required only for PDF ingestion |

---

## Troubleshooting

**`GROQ_API_KEY` not set** → Copy `.env.example` to `.env` and add your key.

**`No documents indexed`** → Ensure `sample_manual.md` exists in `backend/` and the server started without errors.

**FlashRank download slow** → The reranker model downloads ~400 MB on first use. It caches to `/tmp/flashrank`.

**PDF parsing fails** → Set `LLAMA_CLOUD_API_KEY` in `.env`. Markdown files work without it.

**Frontend shows "Disconnected"** → Ensure the backend is running on port 8000. Check CORS.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| API | FastAPI 0.115 + Uvicorn |
| Vector DB | ChromaDB 0.5 |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Sparse Retrieval | BM25Okapi (rank-bm25) |
| Reranking | FlashRank ms-marco-MiniLM-L-12-v2 |
| LLM | Groq LLaMA-3.1-8b-instant |
| PDF Parsing | LlamaParse |
| Evaluation | RAGAS 0.1.19 |
| Frontend | Tailwind CSS + Alpine.js + Marked.js |

---

*Built as a production-grade RAG reference architecture for automotive diagnostics.*
