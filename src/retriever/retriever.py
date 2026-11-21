from src.core.config import config
from src.ingestion.vector_store import vector_store


question = input("Enter your question: ")

retriever = vector_store.as_retriever(search_type=config.SEARCH_TYPE, search_kwargs={"k": config.RETRIEVER_TOP_K})
retrieved_docs = retriever.invoke(question)