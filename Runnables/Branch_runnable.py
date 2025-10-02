from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda
import os
load_dotenv()

prompt = PromptTemplate(
    template = "Write a detail report on {topic}",
    input_variables=['topic']
)

prompt1 = PromptTemplate(
    template = "Summarize the following {text}",
    input_variables=['text']
)

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    api_key=os.getenv('OPENROUTER_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE')
)

parser = StrOutputParser()

report_gen_Chain = RunnableSequence(prompt, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, RunnableSequence(prompt1, model, parser)),
    RunnablePassthrough()
)


final_chain = RunnableSequence(report_gen_Chain,branch_chain)

result = final_chain.invoke({'topic':'Russia Vs Ukraine'})
print(result)