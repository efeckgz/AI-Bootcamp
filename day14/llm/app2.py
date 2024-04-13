import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

key = os.environ['GOOGLE_API_KEY']
genai.configure(api_key=key)

model = genai.GenerativeModel('gemini-pro-vision')


st.title('Analyze image with Google Gemini')

im = st.file_uploader('Pick an image', type=['jpg', 'jpeg', 'png'])
if im is not None:
    im = Image.open(im)
    st.image(im)
    # response = model.generate_content(im)
    # st.write(response.text)

q = st.text_input("Ask away...")
if st.button('Send'):
    response = model.generate_content([q, im], stream=True)
    response.resolve()
    st.write(response.text)