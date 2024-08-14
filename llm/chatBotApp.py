from langchain_community.llms import Ollama
import streamlit as st
from streamlit_chat import message

st.title("ChatBot")

llm = Ollama(model="mistral")

if "messages" not in st.session_state:
    st.session_state.messages = [{'role': 'assistant', 'content': " Hello! Please enter a prompt below!"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Enter prompt here"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    resp = llm.invoke(prompt)

    response = resp
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    
