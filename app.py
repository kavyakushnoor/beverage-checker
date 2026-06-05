import streamlit as st

st.set_page_config(page_title="Beverage Label Checker", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Use the pages above to process beverage labels.")

st.title("🍾 Beverage Label Compliance Checker")

st.write("""
Welcome!  
Use the sidebar to upload images, capture from camera, and review results.
""")
