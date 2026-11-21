from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.ingestion.ingest import documents

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = text_splitter.split_documents(documents)