import streamlit as st
import pandas as pd

st.title("Dashboard")
df=pd.read_excel("dashboard_ok.xlsx","Receitas_Despesas")
st.dataframe(df)
