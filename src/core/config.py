import os
from dotenv import load_dotenv
load_dotenv()   


class Config:
    EMBEDDINGS_MODEL_NAME= "gemini-embedding-2"
    GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY") 
    GROQ_MODEL_NAME= "qwen/qwen3.8-27b"
    GROQ_API_KEY= os.getenv("GROQ_API_KEY") 
    CHUNK_SIZE= 100
    CHUNK_OVERLAP= 20


config = Config()
