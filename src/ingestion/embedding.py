from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.environ.get("GOOGLE_API_KEY") # type: ignore
)
