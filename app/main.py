from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, Base, SessionLocal
from app.models import Document
from app.schemas import DocumentRequest, QuestionRequest
from app.llm import ask_llama
from app.rag import generate_embedding, cosine_similarity

import json

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Knowledge Assistant",
    version="1.0.0"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "AI Knowledge Assistant API Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post(
    "/documents",
    summary="Store a document and generate embeddings"
)
def add_document(
    document: DocumentRequest,
    db: Session = Depends(get_db)
):
    try:
        embedding = generate_embedding(
            document.content
        )

        new_doc = Document(
            content=document.content,
            embedding=json.dumps(embedding)
        )

        db.add(new_doc)
        db.commit()
        db.refresh(new_doc)

        return {
            "message": "Document stored successfully",
            "document_id": new_doc.id
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Document storage failed: {str(e)}"
        )


@app.post(
    "/ask",
    summary="Ask questions using RAG retrieval"
)
def ask_question(
    question: QuestionRequest,
    db: Session = Depends(get_db)
):
    try:
        question_embedding = generate_embedding(
            question.question
        )

        documents = db.query(Document).all()

        if not documents:
            raise HTTPException(
                status_code=404,
                detail="No documents found in database"
            )

        best_document = None
        best_score = -1

        for doc in documents:

            doc_embedding = json.loads(
                doc.embedding
            )

            score = cosine_similarity(
                question_embedding,
                doc_embedding
            )

            if score > best_score:
                best_score = score
                best_document = doc

        answer = ask_llama(
            best_document.content,
            question.question
        )

        return {
            "question": question.question,
            "retrieved_document": best_document.content,
            "similarity_score": float(best_score),
            "answer": answer
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Question answering failed: {str(e)}"
        )