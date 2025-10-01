import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("car_sales_data.csv")

st.bar_chart(df, y="Manufacturer")

st.write(df.head())
