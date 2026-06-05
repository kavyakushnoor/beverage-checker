import streamlit as st
from PIL import Image
from rules import evaluate_rules
from ocr import extract_text

def render():
    st.title("Upload Label Image")

    st.write("Upload one or more beverage label images for compliance checking.")

    uploaded_files = st.file_uploader(
        "Upload label images",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            st.divider()
            st.subheader(file.name)

            image = Image.open(file)
            st.image(image, use_column_width=True)

            with st.spinner("Extracting text..."):
                text = extract_text(image)

            st.subheader("Extracted Text")
            st.text(text)

            with st.spinner("Evaluating rules..."):
                result = evaluate_rules(text)

            st.subheader("Compliance Result")

            if result["status"] == "PASS":
                st.success("PASS")
            elif result["status"] == "WARNING":
                st.warning("WARNING")
            else:
                st.error("FAIL")

            st.write("Issues:")
            if result["issues"]:
                for issue in result["issues"]:
                    st.write(f"- {issue}")
            else:
                st.write("No issues detected.")
