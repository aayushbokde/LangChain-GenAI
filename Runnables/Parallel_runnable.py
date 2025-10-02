from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence
import os
load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a Tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a LinkedIn post about {topic}",
    input_variables=['topic']
)

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    api_key=os.getenv('OPENROUTER_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE')
)

parser = StrOutputParser()

parallelChain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model, parser),
    'linkedIn':RunnableSequence(prompt2, model, parser)
})

result = parallelChain.invoke({'topic':'AI'})

print(result)