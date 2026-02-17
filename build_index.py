from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

from app.config import CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL

def build_index():
    loader = DirectoryLoader("data", glob="**/*.pdf",loader_cls=PyPDFLoader)
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(documents)
    
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vector_db = FAISS.from_documents(chunks, embeddings)
    vector_db.save_local("faiss_index")
    
    print("Vector index built successfully!")


if __name__ == "__main__":
    build_index()
    