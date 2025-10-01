import streamlit as st
import polars as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("car_sales_data.csv")
st.line_chart(df)
