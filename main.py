import streamlit as st

# Meny
# Define the pages
home_page = st.Page("pages/Home.py")
company_page = st.Page("pages/Company.py")
contact_page = st.Page("pages/Contact.py")

# Set up navigation
pg = st.navigation([home_page, company_page, contact_page])

# Run the selected page
pg.run()