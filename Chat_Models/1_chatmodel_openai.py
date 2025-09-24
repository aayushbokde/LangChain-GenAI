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

# temperature is a parameter that controls the randomness of the model's output.
# A higher temperature (e.g., 0.8) will make the output more random
# while a lower temperature (e.g., 0.2) will make it more focused and deterministic.

#max completion tokens is the maximum number of tokens that the model can generate in its response.
# This limits the length of the output.

result = llm.invoke("what is the capital of India?")

print(result) # this will provide the full metadata returned by the model
print(result.content) # this will provide the content only