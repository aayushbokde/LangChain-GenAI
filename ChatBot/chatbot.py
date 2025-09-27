from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()
import os

model = ChatGoogleGenerativeAI(
    model="models/gemini-flash-lite-latest",
    api_key=os.getenv("GOOGLE_API_KEY")
)

chat_history = [
    SystemMessage(content="You are helpful assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Bot:", result.content)

print(chat_history)