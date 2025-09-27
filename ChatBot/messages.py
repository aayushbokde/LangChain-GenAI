from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  
load_dotenv()
import os

model = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
    api_key=os.getenv("GOOGLE_API_KEY")
)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain?"),
                  ]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)