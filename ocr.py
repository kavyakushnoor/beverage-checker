import streamlit as st
import numpy as np
import cv2

# -------------------------
# Safe EasyOCR import
# -------------------------
EASYOCR_AVAILABLE = True

try:
    import easyocr

except Exception as e:

    EASYOCR_AVAILABLE = False
    EASY_OCR_ERROR = str(e)


# -------------------------
# Load OCR model once
# -------------------------
@st.cache_resource
def load_reader():

    if not EASYOCR_AVAILABLE:
        return None

    try:

        return easyocr.Reader(
            ["en"],
            gpu=False
        )

    except Exception:

        return None


reader = load_reader()


# -------------------------
# Image preprocessing
# -------------------------
@st.cache_data
def preprocess(image_array):

    img = image_array.copy()

    h, w = img.shape[:2]

    # avoid divide-by-zero
    if w > 0 and w < 1200:

        scale = 1200 / w

        img = cv2.resize(

            img,

            None,

            fx=scale,

            fy=scale
        )

    # handle grayscale safely
    if len(img.shape) == 3:

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_RGB2GRAY
        )

    else:

        gray = img

    gray = cv2.GaussianBlur(
        gray,
        (3,3),
        0
    )

    gray = cv2.equalizeHist(
        gray
    )

    thresh = cv2.adaptiveThreshold(

        gray,

        255,

        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,

        cv2.THRESH_BINARY,

        11,

        2
    )

    return thresh


# -------------------------
# OCR extraction
# -------------------------
def extract_text(image):

    if not EASYOCR_AVAILABLE:

        return (
            "ocr_error: "
            f"EasyOCR import failed ({EASY_OCR_ERROR})"
        )

    if reader is None:

        return (
            "ocr_error: "
            "OCR backend failed initialization. "
            "Possible PyTorch incompatibility."
        )

    try:

        img = np.array(image)

        processed = preprocess(
            img
        )

        results = reader.readtext(

            processed,

            rotation_info=[
                90,
                180,
                270
            ],

            allowlist=(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "abcdefghijklmnopqrstuvwxyz"
                "0123456789"
                "%().,/:- "
            )
        )

        if not results:

            return ""

        extracted_text = " ".join(

            r[1]

            for r in results
        )

        return extracted_text.lower()

    except Exception as e:

        return f"ocr_error: {str(e)}"