from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

prompt= PromptTemplate(
    template = "Answer the following Question \n {question} from the following text - \n {text}",
    input_variables=['question', 'text']
)

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    api_key=os.getenv('OPENROUTER_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE')
)

parser = StrOutputParser()


url ='https://www.youtube.com/watch?v=bL92ALSZ2Cg&t=1865s'

loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'what is the video that we are talking about', 'text':docs[0].page_content}))
