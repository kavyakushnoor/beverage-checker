import streamlit as st
import numpy as np
import cv2

# Try importing EasyOCR safely
EASYOCR_AVAILABLE = True
try:
    import easyocr
except Exception as e:
    EASYOCR_AVAILABLE = False
    EASY_OCR_ERROR = str(e)


@st.cache_resource
def load_reader():
    """
    Load EasyOCR reader with safe fallback.
    """
    if not EASYOCR_AVAILABLE:
        return None

    try:
        return easyocr.Reader(['en'], gpu=False)
    except Exception as e:
        # PyTorch failure, incompatible Python version, etc.
        return None


reader = load_reader()


@st.cache_data
def preprocess(image_array):
    """
    Preprocess image for OCR: resize, grayscale, blur, equalize, threshold.
    Cached for performance.
    """
    img = image_array.copy()

    # Resize if too small
    h, w = img.shape[:2]
    if w < 1200:
        scale = 1200 / w
        img = cv2.resize(img, None, fx=scale, fy=scale)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Denoise
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Improve contrast
    gray = cv2.equalizeHist(gray)

    # Adaptive threshold
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return thresh


def extract_text(image):
    """
    Extract text using EasyOCR with robust error handling.
    Returns lowercase text or a clear error string.
    """
    # Check if EasyOCR is available
    if not EASYOCR_AVAILABLE:
        return f"ocr_error: EasyOCR failed to import ({EASY_OCR_ERROR})"

    # Check if reader loaded successfully
    if reader is None:
        return (
            "ocr_error: OCR backend failed to initialize. "
            "This usually means PyTorch is incompatible with your Python version."
        )

    try:
        img = np.array(image)
        processed = preprocess(img)

        results = reader.readtext(
            processed,
            rotation_info=[90, 180, 270],
            allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%().,/:- "
        )

        if not results:
            return ""

        text = " ".join([r[1] for r in results])
        return text.lower()

    except Exception as e:
        return f"ocr_error:{str(e)}"
