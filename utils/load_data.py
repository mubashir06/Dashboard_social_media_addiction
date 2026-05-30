import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    df=pd.read_csv(
        "cleaned_social_media.csv"
    )

    return df