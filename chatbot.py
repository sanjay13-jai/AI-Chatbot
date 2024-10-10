from langchain_community.llms import Ollama #software for pre trained data (llama 3.1)
from langchain_core.prompts import ChatPromptTemplate #conversation b/t AI and user
from langchain_core.output_parsers import StrOutputParser #remove specila charcters
import streamlit as st #ui for chatbot

st.title("Hi, I'm Sanjay. This is my AI ChatBot to assist you.")
user_input_text = st.text_input("Please enter your queries here...")

prompt = ChatPromptTemplate.from_messages(
    [("system", "Your a AI assistant, your name is JAISAN"),
    ("user", "your query:{query}")
    ])

llm = Ollama(model="llama3.1")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if user_input_text:
    st.write(chain.invoke({"query": user_input_text}))