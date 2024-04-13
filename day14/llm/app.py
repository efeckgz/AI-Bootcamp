import streamlit as st
import google.generativeai as genai
import os

key = os.environ['GOOGLE_API_KEY']
genai.configure(api_key=key)

st.title('Chat with Google')

model = genai.GenerativeModel('gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

q = st.text_input("You: ")
if st.button("Ask"):
    response = chat.send_message(q)
    st.write(response.text)
    # st.write(chat.history)