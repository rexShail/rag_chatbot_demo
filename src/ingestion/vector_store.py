from langchain_chroma import Chroma
from src.core.config import config
from src.ingestion.splitter import chunks
from src.ingestion.embedding import embeddings

vector_store = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings,
    persist_directory=config.CHROMA_PERSIST_DIRECTORY
)
