import faiss
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.embeddings import LlamaCppEmbeddings

embeddings = LlamaCppEmbeddings(model_path="models/llama-embeddings-tiny.bin")
vector_db = FAISS.from_doccuments(chunks,embeddings)
vector_db.save_local("faiss_index")
print("Completed vector databased and saved")