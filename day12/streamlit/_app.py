import streamlit as st
import pandas as pd
import plotly.express as px

st.title('MLOps streamlit apps :flag-tr:')

menu = ['Intro', 'AI', 'Contact', 'About Us']
st.sidebar.selectbox("Menu", menu)

df = pd.read_csv('data/prog_languages_data.csv')
fig = px.pie(df, values='Sum')
st.plotly_chart(fig)

fig2 = px.bar(df, x='lang', y='Sum')
st.plotly_chart(fig2)

name = st.text_input("Enter name", max_chars=20)
# st.video('data/secret_of_success.mp4')
# st.camera_input('camera')
st.date_input('select date')
st.time_input('select time')
st.text_input('enter password', type='password')
st.text_area('message', height=80)
st.number_input("enter age", 1, 100)
st.radio("Martial status: ", ('Married', 'Bachelor', 'Engaged'))
st.selectbox('Programming languages you know', ['C++', 'Python', 'Java', 'Rust', 'Go'])
st.image('data/image_01.jpg')
df = pd.read_csv('data/iris.csv')
st.table(df)
st.area_chart(df)
st.code('''
    fn main() {
        println!("Hello, world");
    }
''', language='Rust')
st.success("yay!how to flas")
st.error('error!')

st.slider('pick a number', 1, 100)