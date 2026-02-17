from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from .config import EMBEDDING_MODEL, LLM_MODEL, TOP_K


def load_rag_pipeline():
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    
    print("Loading vector database...")
    
    vector_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True,
    )

    retriever = vector_db.as_retriever(search_kwargs={"k": TOP_K})
    print("Retriever loaded successfully!")

    llm = OllamaLLM(model=LLM_MODEL, streaming=True)

    prompt = ChatPromptTemplate.from_template("""
You are an expert assistant answering strictly from the provided Bhagavad Gita context.

Rules:
- Answer ONLY from the given context.
- If answer is not in context, say: "Answer not found in the provided document."
- Keep answer clear and concise (max 150 words).
- Do NOT add outside knowledge.

Context:
{context}

Question:
{question}

Answer:
""")

    # Format retrieved documents
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Modern LCEL RAG chain
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
