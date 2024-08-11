from langchain_community.llms import Ollama
import streamlit as st
from streamlit_chat import message

st.title("ChatBot")

llm = Ollama(model="mistral")


message("Please enter your prompt") 
prompt = st.chat_input("Enter your prompt:")
if prompt:
    message(prompt, is_user=True) 
    resp = llm.invoke(prompt)
    message(resp) 
