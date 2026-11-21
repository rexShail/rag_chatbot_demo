

from src.ingestion.vector_store import vector_store


question = input("Enter your question: ")

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
retrieved_docs = retriever.invoke(question)