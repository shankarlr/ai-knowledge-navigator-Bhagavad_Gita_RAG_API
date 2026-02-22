# Bhagavad Gita RAG API

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system for question answering over the Bhagavad Gita.

The application uses vector embeddings stored in FAISS for semantic retrieval and exposes the querying functionality through a FastAPI backend.

It demonstrates a clean, modular implementation of a backend-focused RAG architecture.

---

## Architecture

The system follows a standard Retrieval-Augmented Generation workflow:

1. Load and preprocess Bhagavad Gita text  
2. Split text into semantic chunks  
3. Generate embeddings  
4. Store embeddings in a FAISS index  
5. Accept user queries via REST API  
6. Retrieve relevant passages  
7. Generate grounded responses using an LLM  

This architecture improves contextual accuracy and reduces hallucination.

---

## Project Structure

```
gita-rag-api/
│
├── app/                  # FastAPI application and RAG logic
├── data/                 # Bhagavad Gita dataset
├── build_index.py        # Script to generate FAISS index
├── requirements.txt      # Project dependencies
├── .gitignore
└── README.md
```

---

## Tech Stack

- Python 3.10+
- FastAPI
- FAISS
- Sentence Transformers
- LLM (OpenAI or local model via Ollama)
- Uvicorn

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gita-rag-api.git
cd gita-rag-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Build the FAISS Index

Before running the API, generate the vector index:

```bash
python build_index.py
```

This step:
- Loads the dataset
- Generates embeddings
- Stores the FAISS index locally

---

## Run the API Server

```bash
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST `/query`

Request:

```json
{
  "question": "What is Karma Yoga?"
}
```

Response:

```json
{
  "question": "What is Karma Yoga?",
  "answer": "Generated response based on retrieved context.",
  "sources": ["Chapter 2, Verse X"]
}
```

---

## Design Principles

- Clear separation between indexing and querying layers
- Modular FastAPI backend
- Local vector store for performance
- Easily extendable architecture

---

## Future Improvements

- Docker containerization
- Cloud deployment
- Authentication
- Conversation memory
- Managed vector database integration

---

## Author

Shankar LR  
Bangalore, India  
