
import streamlit as st

import requests

st.set_option("deprecation.showfileUploaderEncoding", False)
uploaded_file = st.file_uploader("Choose a video", type="mp4")

if uploaded_file is not None:

    # uploaded_file.__dict__
    # uploaded_file

    bytesdata = uploaded_file.read()

    # api call
    url = "http://localhost:8000/predict"
    files = {
        "in_file": bytesdata
    }

    response = requests.post(url, files=files)

    if response.status_code == 200:
        resp = response.json()
        resp
    else:
        "😬 api error 🤖"
