import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

def preprocess(image):
    image = image.resize((30, 30))
    image = np.array(image)
    image = image / 255.0 # Normalize
    image = np.expand_dims(image, axis=0)
    return image

model = load_model('capstone.keras')

st.title("Traffic sign recognition with deep learning :car:")
st.write("Provide an image for the model to predict to which class it belongs.")

file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
if file is not None:
    im = Image.open(file)
    st.image(im, caption='Uploaded image')
    im = preprocess(im)
    prediction = model.predict(im)
    predicted_class = np.argmax(prediction)
    st.write(predicted_class)