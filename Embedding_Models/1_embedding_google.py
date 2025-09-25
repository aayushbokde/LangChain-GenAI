from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Make sure you have set GOOGLE_API_KEY in your .env
# GOOGLE_API_KEY=<your_google_api_key>

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",  # Google's embedding model
)

# Generate embedding
result = embedding.embed_query("what is the capital of India?")
print(str(result))
