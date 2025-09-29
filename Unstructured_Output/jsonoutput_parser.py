from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "models/gemini-flash-lite-latest"
)
parser = JsonOutputParser()

#whenever using jsonoutputparser always provide format instructions to give the output 

template = PromptTemplate(
    template="give me the name, age and city of the fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()} #automatically sets the return type to json
)

# prompt = template.format()
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
# print(type(final_result))

chain = template | model | parser
#we cannot decide the output schema
#it does not enforce any output schema
result = chain.invoke({})
print(result)