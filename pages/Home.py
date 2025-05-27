import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Por Cho",
    page_icon="👋")

colA1, colA2 = st.columns(2)

with colA1:
    st.image("pages/home_data/images/photo.png")
with colA2:
    st.title("Poramate Chotvararak")
    content = """
    Hi, I am Por! I am a Python programmer.
    """
    st.info(content)

msgA = """
Below you can find some of the apps I have built in Python, Feel free to contact me!
"""
st.write(msgA)

proj_data = pd.read_csv("pages/home_data/data.csv",sep=";")
# print(proj_data)

colB1, colB2 = st.columns(2)
with colB1:
    for index, row in proj_data.iterrows():
        if index % 2 == 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image("pages/home_data/images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")

with colB2:
    for index, row in proj_data.iterrows():
        if index % 2 != 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image("pages/home_data/images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")