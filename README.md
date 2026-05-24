# RAG-Based-Technical-Documentation-Assistant

A Retrieval-Augmented Generation (RAG) powered technical documentation assistant built using **LangGraph**, **FastAPI**, **ChromaDB**, and **Google Gemini**.

This project was developed as part of the **AI/ML Engineer Intern Take-Home Assignment** for Express Analytics.

---

# Project Overview

This system allows users to ask natural language questions about technical documentation such as:

- FastAPI
- Pydantic
- LangChain

The assistant retrieves relevant document chunks from a vector database, grades their relevance using an LLM, and generates grounded answers with source citations.

The workflow is implemented using **LangGraph** with a self-corrective retrieval pipeline.

---

# Features

## Core Features

- Retrieval-Augmented Generation (RAG)
- LangGraph workflow orchestration
- Query rewriting
- Semantic document retrieval
- LLM-based document grading
- Context-aware answer generation
- Source citations
- FastAPI REST API
- Local vector database using ChromaDB

---

# Workflow Architecture

```text
User Question
      ↓
Query Rewrite
      ↓
Vector Retrieval
      ↓
Document Grading
      ↓
Relevant Docs?
   ┌───────────────┐
   │ Yes           │ No
   ↓               ↓
Answer          End / Retry
Generation
      ↓
Final Response + Sources
```

---

# Tech Stack

| Component | Technology |
|---|---|
| Backend API | FastAPI |
| Workflow Engine | LangGraph |
| LLM | Google Gemini 1.5 Flash |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Language | Python 3.10 |

---

# Project Structure

```text
rag-tech-assistant/
│
├── app/
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── graph/
│   │   ├── nodes.py
│   │   ├── state.py
│   │   └── workflow.py
│   │
│   ├── ingestion/
│   │   └── ingest.py
│   │
│   ├── llm/
│   │   └── model.py
│   │
│   ├── vectorstore/
│   │   └── db.py
│   │
│   ├── utils/
│   │   └── prompts.py
│   │
│   ├── data/
│   │   └── docs/
│   │       ├── fastapi.md
│   │       ├── pydantic.md
│   │       └── langchain.md
│   │
│   └── main.py
│
├── chroma_db/
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO
cd rag-tech-assistant
```

---

## 2️. Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️. Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Get free API key from:

https://aistudio.google.com

---

# Document Ingestion

The system uses Markdown-based technical documentation.

Current corpus:
- FastAPI documentation
- Pydantic documentation
- LangChain documentation

Run ingestion manually:

```bash
python
```

```python
from app.ingestion.ingest import ingest_documents

chunks = ingest_documents()

print(chunks)
```

This:
- loads documents
- splits them into chunks
- generates embeddings
- stores embeddings in ChromaDB

---

# Running the Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## POST `/query`

Submit a technical question.

### Example Request

```json
{
  "question": "What is dependency injection in FastAPI?"
}
```

### Example Response

```json
{
  "question": "What is dependency injection in FastAPI?",
  "answer": "FastAPI provides dependency injection using Depends()... Sources: ['fastapi.md']"
}
```

---

## POST `/ingest`

Ingest documents into the vector database.

---

## GET `/documents`

List indexed documents.

---

## POST `/feedback`

Submit feedback for generated answers.

---

# Chunking Strategy

The documents are split using:

- Chunk Size: 500
- Chunk Overlap: 100

### Why?

Technical documentation often contains:
- code examples
- API references
- multi-paragraph explanations

Overlapping chunks preserve semantic continuity between sections.

---

# Embedding Strategy

Embedding Model Used:

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Why?

- Lightweight
- Fast
- Strong semantic search performance
- Open-source and free

---

# Self-Corrective RAG

The system uses an LLM-based grading mechanism.

Each retrieved document chunk is evaluated as:

- Relevant
- Irrelevant

Only relevant chunks are passed into answer generation.

This reduces hallucinations and improves answer grounding.

---

# Corpus Sources

The technical corpus was created using curated content from official documentation:

- FastAPI
- Pydantic
- LangChain

The documents were converted into Markdown format for ingestion.

---

# Future Improvements

Potential future enhancements include:

- Hallucination detection node
- Web search fallback
- Conversation memory
- Hybrid search (BM25 + Vector Search)
- Streaming responses
- Frontend UI with Streamlit or React

---

# Example Questions

You can test queries like:

- How does FastAPI dependency injection work?
- What is BaseModel in Pydantic?
- What are vector stores in LangChain?
- Explain Retrieval-Augmented Generation
- What is LangGraph used for?

---

# Design Decisions & Tradeoffs

## Why LangGraph?

LangGraph provides:
- graph-based orchestration
- state management
- conditional routing
- self-corrective workflows

It was ideal for implementing adaptive RAG pipelines.

---

## Why ChromaDB?

- Simple local setup
- No external infrastructure
- Easy integration with LangChain

---

## Why Gemini Flash?

- Fast inference
- Cost efficient
- Good reasoning capability
- Free tier available

---

# Author

Alexander Roy

AI/ML Engineer Intern Assignment Submission

---

# License

This project is intended for educational and assessment purposes.
