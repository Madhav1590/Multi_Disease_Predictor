import app1
import app2
import app3

import streamlit as st

PAGES = {
    "Diabetes Checkup": app1,
    "Heart Disease Checkup": app2,
    "Liver Disease Checkup": app3
}

st.sidebar.title('Multi Disease Predictor')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
