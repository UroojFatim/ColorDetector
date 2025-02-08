import streamlit as st

page_bg_img = '''
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .container {
        display: flex;
        align-items: center;
        position: relative;
    }
    .title {
        margin-bottom: 10px;
        text-align: center;
        color: purple;
        font-family: cursive;
    }
    .paragraph {
        margin-bottom: 20px;
        font-family: cursive;
    }
    .button1 {
        background-color: white;
        color: black;
        border: 2px solid purple;
        border-radius: 10px;
        transition-duration: 0.4s;
        padding: 10px 20px;
        white-space: nowrap;
        font-family: Arial, sans-serif;
        position: relative;
    }
    .button1:hover {
        background-color: purple !important;
        color: white !important;
    }
    .para {
        text-align: justify;
        font-family: Arial, sans-serif;
    }
    .img {
        margin-top: 20px;
        width: 400px;
        height: 400px;
        margin-left: 160px;
        border-radius: 15px;
    }
    .arrow {
        position: absolute;
        top: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 10px solid transparent;
        border-right: 10px solid transparent;
        border-bottom: 10px solid black; /* Arrow color */
    }
    .label {
        position: absolute;
        top: -30px; /* Adjust distance of label from above */
        left: 50%;
        transform: translateX(-50%);
        font-family: Arial, sans-serif;
        font-size: 14px;
        color: black;
    }
    .label {
        back
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">Webcam Color Detection</h1>', unsafe_allow_html=True)

st.markdown('<p class="para">Welcome to our color detection tool, designed with accessibility in mind. We understand that colorblindness can affect the way individuals perceive colors, which is why our tool aims to assist those with color vision deficiencies. With our application, you can accurately identify colors and understand the hues that you may have difficulty distinguishing.</p>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="container">
        <div class="label">Click here to capture image</div>
        <div class="arrow"></div>
        <button class="button1">Capture Image</button>
        <img src="https://img.freepik.com/premium-photo/beautiful-colorful-wallpapers-4k_762785-10350.jpg?w=900" class="img" alt="Image">
    </div>
    """,
    unsafe_allow_html=True
)
