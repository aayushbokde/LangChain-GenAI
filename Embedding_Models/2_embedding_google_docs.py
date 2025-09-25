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

docs = [
    "India is a country in South Asia. It is the seventh-largest country by land area, the second-most populous country, and the most populous democracy in the world. The capital of India is New Delhi.",
    "The capital of Japan is Tokyo. It is the largest city in Japan and one of the most populous metropolitan areas in the world.",
    "The capital of France is Paris. It is known for its art, fashion, gastronomy, and culture."
]

# Generate embedding
result = embedding.embed_documents(docs)
print(str(result))
