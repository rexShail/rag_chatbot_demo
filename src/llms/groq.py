from langchain_groq import ChatGroq 
from src.core.config import config

llm = ChatGroq(
    model=config.GROQ_MODEL_NAME,
    api_key=config.GROQ_API_KEY  # type: ignore
)