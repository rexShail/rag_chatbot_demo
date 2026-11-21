from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.core.config import config


embeddings = GoogleGenerativeAIEmbeddings(
    model=config.EMBEDDINGS_MODEL_NAME,
    google_api_key=config.GOOGLE_API_KEY  # type: ignore
)