import streamlit as st
from pickle import load

st.title("Predict salary based on experience, examination and interview performance :heavy_dollar_sign:")

# pkl file is in day12 folder
model = load(open('salary_lr.pkl', 'rb'))

xp = st.number_input("Experience", 1, 10)
exam = st.number_input("Exam score", 1, 10)
interview = st.number_input("Interview performance", 1, 10)

if st.button("Predict!"):
    pred = model.predict([[xp, exam, interview]])
    pred = round(pred[0][0], 2)
    s = f'Predicted salary: ${pred}'
    st.success(s)