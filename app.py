import streamlit as st

# ---------------------------------------------------
# Top Navigation Bar (always visible, never collapses)
# ---------------------------------------------------
def render_navbar():
    st.markdown("""
        <style>
            .topnav {
                background-color: #0E1117;
                overflow: hidden;
                padding: 10px 0;
                border-bottom: 1px solid #333;
            }
            .topnav a {
                float: left;
                color: #f2f2f2;
                text-align: center;
                padding: 12px 22px;
                text-decoration: none;
                font-size: 18px;
                font-weight: 500;
            }
            .topnav a:hover {
                background-color: #262730;
                color: white;
            }
        </style>

        <div class="topnav">
            <a href="/?page=Home">Home</a>
            <a href="/?page=Camera">Camera Capture</a>
            <a href="/?page=Upload">Upload Label</a>
            <a href="/?page=Rules">Rules</a>
        </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------
# Home Page Content
# ---------------------------------------------------
def render_home():
    st.title("Beverage Label Checker")
    st.write("Welcome! Use the navigation bar above to capture a label, upload an image, or review compliance rules.")

    st.markdown("""
        ### What this app does
        - Extracts text from beverage labels  
        - Applies rule‑based compliance checks  
        - Highlights missing or incorrect elements  
        - Helps ensure regulatory accuracy  
    """)

    st.info("Use the **Camera Capture** or **Upload Label** options to begin.")


# ---------------------------------------------------
# Router (no switch_page → no StreamlitAPIException)
# ---------------------------------------------------
def main():
    st.set_page_config(page_title="Beverage Label Checker", layout="wide")

    render_navbar()

    page = st.query_params.get("page", "Home")

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

    else:
        render_home()


if __name__ == "__main__":
    main()
