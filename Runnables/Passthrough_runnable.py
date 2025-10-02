from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough
import os
load_dotenv()

prompt1 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "explain the following joke - {text}",
    input_variables=['text']
)

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    api_key=os.getenv('OPENROUTER_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE')
)

parser = StrOutputParser()


joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallelChain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2, model, parser)
})  


final_chain = RunnableSequence(joke_gen_chain, parallelChain)

print(final_chain.invoke({'topic':'Cricket'}))