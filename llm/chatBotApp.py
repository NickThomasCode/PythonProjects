from langchain_community.llms import Ollama
import streamlit as st
from streamlit_chat import message

st.title("ChatBot")

llm = Ollama(model="mistral")

import numpy as np

prompt = st.chat_input("Enter your prompt:")
if prompt:
    resp = llm.invoke(prompt)
    st.write(resp)