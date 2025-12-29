import pandas as pd
import numpy as np
import streamlit as st

st.title("Streamlit Text Input")

name=st.text_input("Enter your name: ")


age=st.slider("Select your age: ",0,100,25 )
st.write(f"Your age is, {age}")

options = ["Python","Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language: ", options)
st.write(f"Your favourite language is {choice}.")

if name:
    st.write(f"Hello, {name}")

data = { 
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"] 
    }
   
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_files=st.file_uploader("Choose a CSV file", type="csv")

if uploaded_files is not None:
    df=pd.read_csv(uploaded_files)
    st.write(df)