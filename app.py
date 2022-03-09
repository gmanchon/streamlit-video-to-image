
import streamlit as st

import requests
import shutil
import base64

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

    with requests.post(url, files=files, stream=True) as response:

        if response.status_code == 200:

            # save image https://betterprogramming.pub/how-to-download-streaming-responses-as-a-file-in-python-51b52943f4e7
            local_filename = "downloaded.gif"
            with open(local_filename, "wb") as f:
                shutil.copyfileobj(response.raw, f)

            # display image
            st.image(local_filename)

            # # display image https://discuss.streamlit.io/t/how-to-show-local-gif-image/3408/3
            # with open(local_filename, "rb") as f:

            #     content = f.read()

            #     data_url = base64.b64encode(content).decode("utf-8")
            #     st.markdown(
            #         f'<img src="data:image/gif;base64,{data_url}" alt="the gif">',
            #         unsafe_allow_html=True)

        else:
            "😬 api error 🤖"
