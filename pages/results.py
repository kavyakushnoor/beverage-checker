import streamlit as st
import pandas as pd

st.title("📊 Results")

if "results" not in st.session_state or not st.session_state.results:
    st.warning("No results yet. Upload images or capture from camera.")
    st.stop()

df = pd.DataFrame(st.session_state.results)

st.subheader("Summary Table")
st.dataframe(df[["file", "status", "issues"]], use_container_width=True)

st.subheader("Detailed Results")

for row in st.session_state.results:
    st.divider()
    st.write(f"### {row['file']}")

    if row["status"] == "PASS":
        st.success("PASS")
    elif row["status"] == "WARNING":
        st.warning("WARNING")
    else:
        st.error("FAIL")

    st.write("Issues:", row["issues"] or "None")

    with st.expander("Extracted Text"):
        st.text(row["text"])

csv = df.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    file_name="beverage_results.csv",
    mime="text/csv"
)
