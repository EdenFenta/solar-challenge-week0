import streamlit as st
import matplotlib.pyplot as plt
from utils import load_data, filter_data

# --- Page Configuration ---
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

st.title("☀️ Solar Energy Comparison Dashboard")
st.write("Interactive visualization of solar irradiance metrics across Benin, Sierra Leone, and Togo.")


df = load_data()


st.sidebar.header("Filter Options")
countries = st.sidebar.multiselect(
    "Select Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)
metrics = st.sidebar.multiselect(
    "Select Metric(s)",
    options=["GHI", "DNI", "DHI"],
    default=["GHI"]
)

filtered_df = filter_data(df, countries=countries, metrics=metrics)


col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average Irradiance by Country")
    avg_values = filtered_df.groupby("Country")[metrics].mean()
    st.bar_chart(avg_values)
