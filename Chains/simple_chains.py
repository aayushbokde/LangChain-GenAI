from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template="write five interesting facts about {topic}",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(
    model = "models/gemini-flash-lite-latest"
)

parser = StrOutputParser()

#'|' this is called pipe operator

chain = prompt | model | parser # this is a declarative way of showing the pipeline and also forming chains
result = chain.invoke({'topic':'Cartoons'})

# print(result)

# visualizing chains

chain.get_graph().print_ascii()