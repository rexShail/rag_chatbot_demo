from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq 

import os
from dotenv import load_dotenv

load_dotenv()

loader = DirectoryLoader("data", 
                         glob="**/*.txt", 
                         loader_cls=TextLoader)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = text_splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.environ.get("GOOGLE_API_KEY") # type: ignore
)


vectorstore = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings,
    persist_directory="data/chroma_db")

print("Persisting vectorstore to disk...")
question = input("Enter your question: ")
print(f"Searching for answer to: {question}")

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
retrieved_docs = retriever.invoke(question)
print(f"Retrieved documents: {retrieved_docs}")

content = "\n".join([document.page_content for document  in retrieved_docs])
print(f"Retrieved content: {content}")
prompt_template = ChatPromptTemplate.from_template(
    "You are a Shailender Singh (rexShail) assistant. Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
)   

formatted_prompt = prompt_template.format(context=content, question=question)

llm = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=os.environ.get("GROQ_API_KEY") # type: ignore
)

response = llm.invoke(formatted_prompt)
print(f"Response: {response.content}")  

