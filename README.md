# Bhagavad Gita RAG System

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system for question answering over the Bhagavad Gita.

The application uses vector embeddings stored in FAISS for semantic retrieval and exposes the querying functionality through a FastAPI backend.

It is designed as a clean, modular, backend-focused implementation of a production-style RAG architecture.

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

This approach improves contextual accuracy and reduces hallucination.

---

## Project Structure
