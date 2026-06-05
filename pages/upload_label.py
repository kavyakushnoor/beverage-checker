import streamlit as st
from PIL import Image

from ocr import extract_text
from rules import evaluate_rules


def render():

    st.title("Upload Label Images")

    uploaded_files = st.file_uploader(
        "Upload labels",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    if uploaded_files:

        for file in uploaded_files:

            st.divider()
            st.subheader(file.name)

            image = Image.open(file)

            # Modern Streamlit: container auto-expands image width
            with st.container():
                st.image(image)

            with st.spinner("Extracting text..."):
                text = extract_text(image)

            st.text(text)

            result = evaluate_rules(text)

            if result["status"] == "PASS":
                st.success("PASS")

            elif result["status"] == "WARNING":
                st.warning("WARNING")

            else:
                st.error("FAIL")

            st.write(
                result["issues"]
                if result["issues"]
                else "No issues"
            )

            st.session_state.results.append({
                "file": file.name,
                "status": result["status"],
                "issues": ",".join(result["issues"]),
                "text": text
            })
