import streamlit as st
from PIL import Image
from rules import evaluate_rules
from ocr import extract_text

def render():
    st.title("Camera Capture")

    st.write("Capture an image of a beverage label using your device camera.")

    image_file = st.camera_input("Take a picture")

    if image_file:
        image = Image.open(image_file)

        st.subheader("Captured Image")
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
