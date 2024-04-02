import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

def process_image(im):
    im = im.resize((170, 170))
    im = np.array(im)
    im = im / 255.0
    im = np.expand_dims(im, axis=0)
    return im

model = load_model('my_cnn_model.h5')

st.title("Skin cancer recognition with deep learning :cancer:")
st.write("Provide an image, and the model will determine weather it is skin cancer or not.")

file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
if file is not None:
    im = Image.open(file)
    st.image(im, caption="uploaded image")
    im = process_image(im)
    prediction = model.predict(im)
    predicted_class = np.argmax(prediction)

    class_names = ['Cancer', 'Not Cancer']
    st.write(class_names[predicted_class])

