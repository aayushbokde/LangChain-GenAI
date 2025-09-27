from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage


chat_template = ChatPromptTemplate([
    ('system', 'You are helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
    # SystemMessage(content = "You are helpful {domain} expert"),
    # HumanMessage(content = "Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'dusra'})

print(prompt)

#this does the same thing as prompt template, but prompt template is user for single turn query or session
#but chatprompttemplate is used for multiturn conversations