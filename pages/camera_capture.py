import streamlit as st
from PIL import Image
from ocr import extract_text
from rules import evaluate_rules

st.title("📸 Capture From Camera")

if "results" not in st.session_state:
    st.session_state.results = []

image_file = st.camera_input("Capture image")

if image_file:
    image = Image.open(image_file)
    text = extract_text(image)
    result = evaluate_rules(text)

    st.session_state.results.append({
        "file": "camera_capture",
        "status": result["status"],
        "issues": "; ".join(result["issues"]),
        "text": text
    })

    st.success("Image processed! View results in the Results page.")
