import streamlit as st
from send_email import send_email

st.set_page_config(
    layout="wide",
    page_title="Contact Me",
    page_icon="📞")

st.title("Contact Me")
with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    user_raw_msg = st.text_area("Your message")
    user_msg = f"""\
Subject: New message from {user_email}

From: {user_email}
{user_raw_msg}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(user_msg)
        st.info("Your message was sent successfully.")

# st.session_state

