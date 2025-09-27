from langchain_openrouter import OpenRouterEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding = OpenRouterEmbeddings(
    model="text-embedding-3-small",
    openrouter_api_key=os.getenv("OPENROUTER_API_KEY")
)

result = embedding.embed_query("what is the capital of India?")
print(result)
