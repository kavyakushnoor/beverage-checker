import streamlit as st
import json


def render():

    st.title(
        "Compliance Rules"
    )

    with open(

        "configs/beverage_rules.json",

        "r"

    ) as f:

        rules = json.load(f)

    st.write(
        """
These rules determine whether
a beverage label passes compliance.
"""
    )

    st.subheader(
        "Required Words"
    )

    for word in rules[
        "required_words"
    ]:

        st.write(
            f"• {word}"
        )

    st.subheader(
        "Mandatory Phrases"
    )

    for phrase in rules[
        "must_contain"
    ]:

        st.write(
            f"• {phrase}"
        )

    st.info(
        "Multiple missing items "
        "may result in FAIL."
    )