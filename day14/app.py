import streamlit as st
from pycaret.classification import setup, compare_models, pull, save_model, load_model
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import ydata_profiling
import os

def upload_screen():
    st.title('Upload')
    file = st.file_uploader('Chose file to upload')
    if file:
        df = pd.read_csv(file, index_col=None)
        st.session_state['df'] = df
        st.dataframe(df.head())

def eda_screen():
    st.title('Exploratory Data Analysis')
    if 'df' in st.session_state:
        profile_df = st.session_state['df'].profile_report()
        st_profile_report(profile_df)
    else:
        st.write('Head to the upload section to upload a file.')

def modelling_screen():
    st.title('Modelling')
    if 'df' in st.session_state:
        data = st.session_state['df']
        target = st.selectbox('Choose a target column', data.columns)
        if st.button('Train model'):
            setup(data, target=target)
            setup_df = pull()
            st.dataframe(setup_df)
            best_model = compare_models()
            compare_df = pull()
            st.dataframe(compare_df)
            save_model(best_model, 'bestmodel')
    else:
        st.write('Head to the upload section to upload a file.')


def download_screen():
    with open('best_model.pkl', 'rb') as f:
        st.download('Download best model', )


# Screen name constants
upload = 'Upload'
eda = 'EDA'
modelling = 'Modelling'
download = 'Download'

if 'df' not in st.session_state:
    st.session_state['df'] = None

if os.path.exists('/dataset.csv'):
    df = pd.read_csv('/dataset.csv')
    st.session_state['df'] = df

with st.sidebar:
    st.image('https://cdn0.iconfinder.com/data/icons/machine-learning-flat/60/021_Decision_Making-1024.png')
    st.title('AutoML Classification')
    choice = st.radio('Navigation', [upload, eda, modelling, download])

if choice == upload:
    upload_screen()

if choice == eda:
    eda_screen()

if choice == modelling:
    modelling_screen()

if choice == download:
    download_screen()