from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


import os
from dotenv import load_dotenv

load_dotenv()

loader = DirectoryLoader("data", 
                         glob="**/*.txt", 
                         loader_cls=TextLoader)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = text_splitter.split_documents(docs)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.environ.get("GOOGLE_API_KEY") # type: ignore
)

print(f"Number of chunks: {len(chunks)}")
print(f"Embedding for first chunk: {embeddings.embed_query(chunks[0].page_content)}")

vectorstore = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings,
    persist_directory="data/chroma_db")

print("Persisting vectorstore to disk...")
print(f"Persist directory: {vectorstore}")    

question = input("Enter your question: ")
print(f"Searching for answer to: {question}")

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
retrieved_docs = retriever.invoke(question)
print(f"Retrieved documents: {retrieved_docs}")