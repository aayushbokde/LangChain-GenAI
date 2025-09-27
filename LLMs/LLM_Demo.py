
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

result =llm.invoke("Tell me the capital of India.")
print(result.content)