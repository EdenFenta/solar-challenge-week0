import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """Load and combine cleaned CSVs from all three countries."""
    benin = pd.read_csv("data/benin_clean.csv")
    sierra = pd.read_csv("data/sierra_leone_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")
    
    benin["Country"] = "Benin"
    sierra["Country"] = "Sierra Leone"
    togo["Country"] = "Togo"
    
    return pd.concat([benin, sierra, togo], ignore_index=True)

def filter_data(df, countries=None, metrics=None):
    """Filter dataframe by selected countries and metrics."""
    if countries is not None:
        df = df[df["Country"].isin(countries)]
    if metrics is not None:
        df = df[["Country"] + metrics]
    return df
