# app.py

import streamlit as st
import os
from dotenv import load_dotenv
from src.crew import start_crew  #  Correct import (keep 'src.crew')

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Assignment Generator", page_icon="🤖", layout="centered")

st.title(" AI Assignment Generator")
st.write("Generate Market Research, AI/ML/GenAI Use Cases, and Dataset Resources!")

company_name = st.text_input("Enter the Company Name:")

if st.button("Generate AI Assignment"):
    if company_name.strip() == "":
        st.warning("Please enter a company name first.")
    else:
        with st.spinner("Running agents and generating report..."):
            output = str(start_crew(company_name))   # Always cast to string
            st.success(" Assignment generated successfully!")

            st.subheader(" Final Output:")
            st.markdown(output)

            st.download_button(
                label=" Download Report",
                data=output,
                file_name=f"{company_name.replace(' ', '_')}_AI_Assignment.md",
                mime="text/markdown"
            )
