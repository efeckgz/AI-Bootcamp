import streamlit as st
import pandas as pd

st.title("Taking input from form and saving in csv file")

# d = {
#     'name': [],
#     'password': [],
#     'dob': [],
#     'message': []
# }

# df = pd.DataFrame(d)

# Form
name = st.text_input("Enter your name")
password = st.text_input("Enter password", type='password')
dob = st.date_input("Enter your date of birth", format="DD.MM.YYYY")
# age = st.slider("Enter your age", 1, 100)
message = st.text_area("Whats on your mind", height=80)

# Submit
if st.button('Submit'):
    user = {
        'name': name,
        'password': password,
        'dob': dob,
        'message': message
    }

    df = pd.DataFrame(user)
    st.table(df)
