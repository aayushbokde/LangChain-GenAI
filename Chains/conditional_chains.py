from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
import os
from langchain.schema.runnable import RunnableBranch, RunnableLambda

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

model = ChatOpenAI(
    model = 'gpt-4o-mini',
    api_key=os.getenv('OPENROUTER_API_KEY'),
    base_url=os.getenv('OPENAI_API_BASE')
)

parser = StrOutputParser()

class feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description="give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template = "Classify the feedback of Restaurant to either positive or negative. \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = "write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback'] 
)

prompt3 = PromptTemplate(
    template = "write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback'] 
)
branch_chain = RunnableBranch(
   (lambda x:x.sentiment == "positive", prompt2 | model | parser),  #(lambda x:x['sentiment'] == "positive", prompt2 | model | parser) this is incorrect because feedback is pydantic object and it should be accessed via Attribute and not dictionary style indexing
   (lambda x:x.sentiment == "negative", prompt3 | model |parser),
   RunnableLambda(lambda x : "could not find sentiment") # this isn't a chain so we have to convert it into a runnable using runnable lambda
)

chain = classifier_chain | branch_chain
result = chain.invoke({'feedback':"This is a good restaurant"})

# print(result)

# classifier_chain.get_graph().print_ascii()
# print(f"prompt2 : {prompt2}")
# print(f"prompt3 : {prompt3}")

# branch_chain.get_graph().print_ascii()
chain.get_graph().print_ascii()