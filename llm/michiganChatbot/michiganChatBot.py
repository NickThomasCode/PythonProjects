# import the needed packages
import streamlit as st
from transformers import pipeline


# create pieline for QA
# not specifying a model so huggingface will default to distilbert
qa = pipeline('question-answering')

ctx = "michigan is the greatest university in the world. Michigan is better than Ohio State Michigan State and always will be. Michigan won the last game against Ohio State (OSU) 13-10. Michigan won the last game against Michigan State (MSU) 24-17."

# # que = "What does Nick enjoy doing with free time?"
# # qa(context = ctx, question = que)

# st.title("ChatBot")

# if "messages" not in st.session_state:
#     st.session_state.messages = [{'role': 'assistant', 'content': " Hello! Please enter a prompt below!"}]

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # React to user input
# if prompt := st.chat_input("Enter prompt here"):
#     # Display user message in chat message container
#     st.chat_message("user").markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     resp = qa(context = ctx, question = prompt)

#     response = (resp['answer'])

#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": response})


import streamlit as st

# Mock function for qa(context, question)
# Replace this with the actual implementation of your `qa` function
# def qa(context, question):
#     # Simulate generating an answer based on context and question
#     return {"answer": f"This is a response to: '{question}' based on context '{context}'"}

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = [{'role': 'assistant', 'content': "Hello! Please enter a prompt below!"}]

assistant_image = "data:image/png;base64,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"  # Replace with your assistant's custom image URL or local path
user_image = "data:image/png;base64,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"       # Replace with your user's custom image URL or local path


# Input form for user prompt
with st.form("chat_form", clear_on_submit=True):
    prompt = st.text_input("Enter your message:", placeholder="Type your prompt here...")
    submitted = st.form_submit_button("Send")

# Handle form submission
if submitted and prompt:
    # Clear the chat history
    st.session_state.messages.clear()

    # Display user message
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="background-color: rgba(0, 0, 128, 0.8); color: white; padding: 10px; border-radius: 10px; margin-left: 80%;">
                {prompt}
            </div>
            <img src="{user_image}" alt="User" style="width: 40px; height: 40px; margin-left: 10px; border-radius: 50%;">
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Add user message to session state (optional for single interaction)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate assistant response
    resp = qa(context=ctx, question=prompt)
    response = resp['answer']

    # Display assistant response
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="{assistant_image}" alt="Assistant" style="width: 40px; height: 40px; margin-right: 10px; border-radius: 50%;">
            <div style="background-color: #FBEC5D; color: black; padding: 10px; border-radius: 10px;">
                {response}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Add assistant response to session state (optional for single interaction)
    st.session_state.messages.append({"role": "assistant", "content": response})