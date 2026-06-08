from pydantic import BaseModel


class DocumentRequest(BaseModel):
    content: str


class QuestionRequest(BaseModel):
    question: str
