from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda
import os
load_dotenv()

prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    api_key=os.getenv('OPENROUTER_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE')
)

parser = StrOutputParser()


def word_count(text):
    return len(text.split())


joke_gen_chain = RunnableSequence(prompt, model, parser)

parallelChain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallelChain)

print(final_chain.invoke({'topic':'AI'}))