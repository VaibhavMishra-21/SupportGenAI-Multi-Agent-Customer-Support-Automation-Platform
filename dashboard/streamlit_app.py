import streamlit as st

from workflows.support_workflow import (
    run_support_workflow
)

st.title(
    "SupportGenAI"
)

query = st.text_area(
    "Enter Customer Query"
)

if st.button(
    "Analyze"
):

    result = run_support_workflow(
        query
    )

    st.json(result)
