from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    PyPDFLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_loader = DirectoryLoader(
    path="docs",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader,
)

txt_loader = DirectoryLoader(
    path="docs",
    glob="**/*.txt",
    loader_cls=TextLoader,
)

documents = []
documents.extend(pdf_loader.load())
documents.extend(txt_loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=300)
chunks = splitter.split_documents(documents)
print(f"chunks:{ len(chunks)}")
