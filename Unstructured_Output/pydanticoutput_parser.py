from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
from pydantic import BaseModel, Field

model = ChatGoogleGenerativeAI(
    model = "models/gemini-flash-lite-latest"
)

class Person(BaseModel):
    name:str = Field(description="Name of the person")
    age:int = Field(description="Age of the person")
    ciyt:str = Field(description="name of the city person belongs to")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'generate the name, age and city of fictional person from {place} \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain = template | model | parser
# prompt = template.invoke('India')

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

result = chain.invoke({'place':'India'})

print(result)