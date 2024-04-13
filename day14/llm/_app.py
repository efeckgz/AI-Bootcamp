from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_answer(question):
    answer = chat.send_message(question, stream=True)
    return answer

st.title("Talk to Google Gemini")
prompt = st.text_input('Ask a question', key='input')
submit = st.button('Go')
if submit:
    answer = get_answer(prompt)
    st.header('Answer')
    for chunk in answer:
        st.write(chunk.text)
