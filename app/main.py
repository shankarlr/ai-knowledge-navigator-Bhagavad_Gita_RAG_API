from fastapi import FastAPI
from pydantic import BaseModel
from .rag_pipeline import load_rag_pipeline

app = FastAPI(title="AI Knowledge Navigator - Modern RAG")

rag_chain = load_rag_pipeline()


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/ask")
def ask_question(request: QueryRequest):
    answer = rag_chain.invoke(request.question)
    return {"answer": answer}
