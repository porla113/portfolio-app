import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="The Best Company",
    page_icon="🎉")

st.title("The Best Company")
company_description = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam a fermentum lorem, nec dapibus ipsum. Vivamus ultricies gravida quam eget viverra. Vivamus feugiat bibendum lacus, vitae finibus mi ornare quis. Pellentesque non lacus consectetur, sodales magna sed, efficitur erat. Fusce non dui nibh. Fusce ac dapibus turpis. Mauris metus nunc.
"""
st.write(company_description)
st.header("Our Team")

employee_df = pd.read_csv("pages/company_data/company_data.csv")

colA1, colA2, colA3 = st.columns(3)

with colA1:
    for index, row in employee_df[:4].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image(f"pages/company_data/company_images/{row['image']}")

with colA2:
    for index, row in employee_df[4:8].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image(f"pages/company_data/company_images/{row['image']}")

with colA3:
    for index, row in employee_df[8:].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image(f"pages/company_data/company_images/{row['image']}")