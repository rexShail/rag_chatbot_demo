from langchain_groq import ChatGroq 
import os
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=os.environ.get("GROQ_API_KEY") # type: ignore
)