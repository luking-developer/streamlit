import streamlit as st
import polars as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("car_sales_data.csv")

st.bar_chart(df, x="Manufacturer", y="Engine size")

st.write(df.head())
