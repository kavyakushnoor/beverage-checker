import streamlit as st
import pandas as pd


def render():

    st.title("Results Dashboard")

    if not st.session_state.results:
        st.warning("No results available.")
        return

    df = pd.DataFrame(st.session_state.results)

    st.subheader("Summary")

    total = len(df)
    passes = (df["status"] == "PASS").sum()
    warnings = (df["status"] == "WARNING").sum()
    fails = (df["status"] == "FAIL").sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Tests", total)
    c2.metric("PASS", passes)
    c3.metric("WARNING", warnings)
    c4.metric("FAIL", fails)

    st.divider()

    st.subheader("Recent Result")

    latest = st.session_state.results[-1]

    st.write(f"File: {latest['file']}")
    st.write(f"Status: {latest['status']}")
    st.write(f"Issues: {latest['issues']}")

    st.divider()

    st.subheader("All Results")

    st.dataframe(df)

    csv = df.to_csv(index=False)

    st.download_button(
        "Download CSV",
        csv,
        file_name="beverage_results.csv",
        mime="text/csv"
    )
