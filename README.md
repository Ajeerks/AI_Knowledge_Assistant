# AI Knowledge Assistant

## Overview

AI Knowledge Assistant is a Retrieval-Augmented Generation (RAG) application built using FastAPI, PostgreSQL, Sentence Transformers, and Groq-hosted Llama 3.1.

The system stores documents in PostgreSQL, generates embeddings for semantic search, retrieves the most relevant document using cosine similarity, and generates answers using Llama 3.1 based on the retrieved context.

---

## Features

* FastAPI REST API
* PostgreSQL Database Integration
* Document Storage
* Embedding Generation using Sentence Transformers
* Semantic Search using Cosine Similarity
* Groq Llama 3.1 Integration
* Retrieval-Augmented Question Answering (RAG)

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

## Setup Instructions

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Configure Environment Variables

Create a `.env` file:

DATABASE_URL=postgresql://postgres:password@localhost:5432/ai_assignment

GROQ_API_KEY=your_groq_api_key

### 3. Run the Application

uvicorn app.main:app --reload

### 4. Open Swagger UI

http://127.0.0.1:8000/docs

---

## API Endpoints

### POST /documents

Stores a document and generates its embedding.

Example Request:

{
"content": "CareerPilot was founded in 2024."
}

### POST /ask

Retrieves the most relevant document and generates an answer.

Example Request:

{
"question": "When was CareerPilot founded?"
}

---

## Sample Response

{
"question": "When was CareerPilot founded?",
"retrieved_document": "CareerPilot was founded in 2024.",
"similarity_score": 0.86,
"answer": "CareerPilot was founded in 2024."
}

---

## Author

Ajeer KS
