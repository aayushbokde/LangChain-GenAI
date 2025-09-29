from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "models/gemini-flash-lite-latest"
)

schema = [
    ResponseSchema(name = 'fact_1', description='Fact1 about the topic'),
    ResponseSchema(name = 'fact_2', description='Fact2 about the topic'),
    ResponseSchema(name = 'fact_3', description='Fact3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template="Give 3 facts about {topic} \n {format_instruction} ",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

# prompt = template.invoke({'topic':'blackhole'})

# result= model.invoke(prompt)

# final_result = parser.parse(result.content)
result = chain.invoke({'topic':'blackhole'})

print(result)
