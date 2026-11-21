from langchain_groq import ChatGroq 
from src.core.config import config


llm = ChatGroq(
    model=congig.GROQ_MODEL,  # type: ignore
    api_key=config.GROQ_API_KEY  # type: ignore
)