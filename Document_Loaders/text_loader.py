from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

loader = TextLoader('C:/Users/aayus/Downloads/Langchain+GenAI/Document_Loaders/cricket.txt', encoding = 'utf-8')

docs = loader.load()



model = ChatOpenAI(
    model = 'gpt-4o-mini',
    api_key=os.getenv('OPENROUTER_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE')
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'Write a summary for following poem {poem}',
    input_variables=['poem']
)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))



# print(type(docs))

# print(len(docs))

# print(docs[0])