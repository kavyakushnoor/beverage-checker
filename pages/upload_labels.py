import streamlit as st
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from ocr import extract_text
from rules import evaluate_rules

st.title("📤 Bulk Upload Labels")

if "results" not in st.session_state:
    st.session_state.results = []

def process_image(file_obj, file_name):
    image = Image.open(file_obj)
    text = extract_text(image)
    result = evaluate_rules(text)
    return {
        "file": file_name,
        "status": result["status"],
        "issues": "; ".join(result["issues"]),
        "text": text
    }

uploaded_files = st.file_uploader(
    "Upload beverage labels",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    progress = st.progress(0)

    jobs = [(f, f.name) for f in uploaded_files]

    with ThreadPoolExecutor() as executor:
        for idx, res in enumerate(executor.map(lambda x: process_image(*x), jobs)):
            st.session_state.results.append(res)
            progress.progress((idx + 1) / len(uploaded_files))

    st.success("Processing complete! Go to the Results page.")
