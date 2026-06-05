import streamlit as st
from PIL import Image

from ocr import extract_text
from rules import evaluate_rules


def render():

    st.title("Camera Capture")

    image_file = st.camera_input(
        "Capture beverage label"
    )

    if image_file:

        image = Image.open(image_file)

        # Modern Streamlit: container auto-expands image width
        with st.container():
            st.image(image)

        with st.spinner("Extracting text..."):
            text = extract_text(image)

        st.subheader("Extracted Text")
        st.text(text)

        result = evaluate_rules(text)

        st.subheader("Compliance Result")

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

        # Store results in session state
        st.session_state.results.append({
            "file": "camera_capture",
            "status": result["status"],
            "issues": ",".join(result["issues"]),
            "text": text
        })
