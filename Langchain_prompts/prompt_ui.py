from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate, load_prompt


st.header("<<<< Research Tool >>>>")

# user_input = st.text_input("Enter your query here:")
paper_input=st.selectbox( "Select Research Paper Name", ["Select...", "Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])
style_input=st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input=st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

template = load_prompt("template.json")


if st.button("Submit"):
    # forming the chain
    chain = template | llm
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    
    st.write(result.content)