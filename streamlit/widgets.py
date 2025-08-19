import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input")

name=st.text_input("Enter your name: ")

age=st.slider("Select your age:", 0,100,25)

st.write(f"Age is {age}")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("choose your favorite language:", options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello {name}")

