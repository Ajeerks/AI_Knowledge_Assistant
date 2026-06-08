# AI Knowledge Assistant

## Overview

AI Knowledge Assistant is a Retrieval-Augmented Generation (RAG) application built using FastAPI, PostgreSQL, Sentence Transformers, and Groq-hosted Llama 3.1.

The system stores documents in PostgreSQL, generates vector embeddings for semantic search, retrieves the most relevant document using cosine similarity, and generates context-aware answers using Llama 3.1 based on the retrieved content.

---

## Live Deployment

**Application URL**

https://ai-knowledge-assistant-kv1e.onrender.com

**API Documentation**

https://ai-knowledge-assistant-kv1e.onrender.com/docs

---

## Features

* FastAPI REST API
* PostgreSQL Database Integration
* Document Storage
* Embedding Generation using Sentence Transformers
* Semantic Search using Cosine Similarity
* Retrieval-Augmented Generation (RAG)
* Groq Llama 3.1 Integration
* Error Handling
* Health Check Endpoint
* Cloud Deployment on Render

---

## Tech Stack

* Python 3.10
* FastAPI
* PostgreSQL
* SQLAlchemy
* Sentence Transformers (all-MiniLM-L6-v2)
* NumPy
* Groq API
* Llama 3.1 8B Instant
* Render

---

## Libraries Used

| Library               | Purpose                         |
| --------------------- | ------------------------------- |
| FastAPI               | REST API Development            |
| SQLAlchemy            | Database ORM                    |
| Psycopg2              | PostgreSQL Connector            |
| Sentence Transformers | Embedding Generation            |
| NumPy                 | Cosine Similarity Calculation   |
| Groq                  | LLM Integration                 |
| Python-Dotenv         | Environment Variable Management |

---

## Project Architecture

### Document Processing Flow

Document Upload

↓

Generate Embedding

↓

Store Document + Embedding in PostgreSQL

---

### Question Answering Flow

User Question

↓

Generate Question Embedding

↓

Cosine Similarity Search

↓

Retrieve Relevant Document

↓

Groq Llama 3.1

↓

Generate Answer

---

## API Endpoints

### GET /

Home endpoint

Response:

```json
{
  "message": "AI Knowledge Assistant API Running"
}
```

### GET /health

Health check endpoint

Response:

```json
{
  "status": "healthy"
}
```

### POST /documents

Stores a document and generates embeddings.

Request:

```json
{
  "content": "CareerPilot was founded in 2024."
}
```

Response:

```json
{
  "message": "Document stored successfully",
  "document_id": 1
}
```

### POST /ask

Retrieves the most relevant document and generates an answer.

Request:

```json
{
  "question": "When was CareerPilot founded?"
}
```

Response:

```json
{
  "question": "When was CareerPilot founded?",
  "retrieved_document": "CareerPilot was founded in 2024.",
  "similarity_score": 0.8623,
  "answer": "CareerPilot was founded in 2024."
}
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Ajeerks/AI_Knowledge_Assistant.git
cd AI_Knowledge_Assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
GROQ_API_KEY=your_groq_api_key
```

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

### 5. Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Deployment

The application is deployed on Render and publicly accessible.

**Live Application**

https://ai-knowledge-assistant-kv1e.onrender.com

**Swagger Documentation**

https://ai-knowledge-assistant-kv1e.onrender.com/docs

---

## Author

**Ajeer KS**

BCA Graduate | AI & Machine Learning Enthusiast

GitHub: https://github.com/Ajeerks
