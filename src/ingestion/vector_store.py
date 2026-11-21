from langchain_chroma import Chroma

from src.ingestion.splitter import chunks
from src.ingestion.embedding import embeddings

vector_store = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings,
    persist_directory="data/chroma_db"
)
