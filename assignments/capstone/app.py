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

# Taken from https://huggingface.co/spaces/drmurataltun/capstone/blob/main/app.py
class_names=[
    "Hız sınırı (20km/s)", "Hız sınırı (30km/s)", "Hız sınırı (50km/s)", "Hız sınırı (60km/s)", "Hız sınırı (70km/s)",
    "Hız sınırı (80km/s)", "Hız sınırı sonu (80km/s)", "Hız sınırı (100km/s)", "Hız sınırı (120km/s)", "Geçiş yasağı",
    "3.5 ton üstü araç geçişi yasak", "Kavşakta geçiş hakkı", "Ana yol", "Yol ver", "Dur", "Araç girişi yasak",
    "3.5 ton üstü araç girişi yasak", "Giriş yasak", "Genel dikkat", "Tehlikeli sol viraj", "Tehlikeli sağ viraj",
    "Çift viraj", "Engebeli yol", "Kaygan yol", "Yol sağdan daralıyor", "Yol çalışması", "Trafik ışıkları", "Yaya geçidi",
    "Çocuk geçidi", "Bisiklet geçidi", "Buzlanma/kar dikkati", "Yabani hayvanlar geçebilir", "Hız ve geçiş limitlerinin sonu",
    "İleri sağa dön", "İleri sola dön", "Sadece düz gidin", "Düz git veya sağa dön", "Düz git veya sola dön", "Sağdan devam et",
    "Soldan devam et", "Döner kavşak zorunlu", "Geçiş yasağı sonu", "3.5 ton üstü geçiş yasağı sonu"
]

st.title("Traffic sign recognition with deep learning :car:")
st.write("Provide an image for the model to predict to which class it belongs.")

file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
if file is not None:
    im = Image.open(file)
    st.image(im, caption='Uploaded image')
    im = preprocess(im)
    prediction = model.predict(im)
    predicted_class = np.argmax(prediction)
    st.write(class_names[predicted_class])