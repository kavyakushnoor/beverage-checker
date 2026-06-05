import streamlit as st

st.set_page_config(
    page_title="Beverage Label Checker",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide sidebar completely
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display:none;
}

.block-container{
    padding-top:1rem;
}

div.stButton > button {
    width:100%;
}
</style>
""", unsafe_allow_html=True)


# -------------------------
# Session state
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "results" not in st.session_state:
    st.session_state.results = []


# -------------------------
# Navigation helper
# -------------------------
def navigate(page):

    st.session_state.page = page
    st.rerun()


# -------------------------
# Pretty Top Navigation Bar (Working Navigation)
# -------------------------
st.markdown("""
<style>

.navbar {
    display: flex;
    justify-content: center;
    gap: 2rem;
    background-color: #0E1117;
    padding: 1rem 0;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    border: 1px solid #333;
}

.nav-item {
    color: #e0e0e0;
    font-size: 18px;
    font-weight: 500;
    padding: 0.4rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.25s ease;
    text-decoration: none;
}

.nav-item:hover {
    background-color: #262730;
    color: white;
}

.nav-active {
    background-color: #4CAF50;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# Render navbar using Streamlit buttons disguised as HTML
cols = st.columns(5)

def nav_button(col, label, page):
    active = "nav-active" if st.session_state.page == page else ""
    with col:
        if st.button(label, key=page):
            st.session_state.page = page
            st.rerun()
        st.markdown(f"<div class='nav-item {active}'></div>", unsafe_allow_html=True)


nav_button(cols[0], "Home", "Home")
nav_button(cols[1], "Camera Capture", "Camera")
nav_button(cols[2], "Upload Label", "Upload")
nav_button(cols[3], "Rules", "Rules")
nav_button(cols[4], "Results", "Results")

st.divider()

# -------------------------
# Home
# -------------------------
def render_home():

    st.title("Beverage Label Checker")

    st.write(
        "Capture or upload beverage labels and "
        "automatically validate compliance."
    )

    st.markdown("""
### Features

- OCR text extraction  
- Compliance validation  
- Camera capture  
- Batch uploads  
- Results dashboard  
- CSV export  

### Workflow

1. Upload / Capture label  
2. OCR extraction  
3. Rule validation  
4. Review results  
5. Export findings  
""")


# -------------------------
# Router
# -------------------------
page = st.session_state.page

if page == "Home":

    render_home()

elif page == "Camera":

    import pages.camera_capture as cam
    cam.render()

elif page == "Upload":

    import pages.upload_label as upl
    upl.render()

elif page == "Rules":

    import pages.rules_page as rules
    rules.render()

elif page == "Results":

    import pages.results as results
    results.render()