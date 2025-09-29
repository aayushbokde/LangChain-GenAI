from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "models/gemini-flash-lite-latest"
)

#1st prompt

template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables = ['topic']
)
#2nd prompt

template2 = PromptTemplate(
    template = "write a 5 line summary about the following text report on text. /n {topic}",
    input_variables=['topic']
)

prompt1 = template1.invoke({'topic':'blackhole'})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'topic':'blackhole'})
result2 = model.invoke(prompt2)

print(result2.content)