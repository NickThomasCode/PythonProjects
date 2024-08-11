from langchain_community.llms import Ollama
import streamlit as st
from streamlit_chat import message

st.title("ChatBot")

llm = Ollama(model="mistral")

if "messages" not in st.session_state:
    st.session_state.messages = []

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

    response = f"Default"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
# message("Please enter your prompt") 
# prompt = st.chat_input("Enter your prompt:")
# if prompt:
#     message(prompt, is_user=True) 
#     # resp = llm.invoke(prompt)
#     resp = 'default'
#     message(resp) 
    
