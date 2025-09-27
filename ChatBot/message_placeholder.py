from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

#chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'), # generally messageplace holder is used for retreiving and storing the chat history
    ('human', '{query}')
])


#chat History
chat_history=[]
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())



#giving the history to the chat

#chat Prompts

prompt = chat_template.invoke({'chat_history':chat_history, 'query': 'where is my refund'})

print(prompt)