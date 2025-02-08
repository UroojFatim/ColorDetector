import streamlit as st
import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
import webcolors

# Function to get dominant color from an image
def get_dominant_color(image, k=5):
    # Convert image to RGB (OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    # Apply KMeans to find dominant colors
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(image)
    colors = kmeans.cluster_centers_
    labels = kmeans.labels_
    label_counts = Counter(labels)
    # Find the most common color, excluding grayscale colors
    for color in label_counts.most_common():
        dominant_color = colors[color[0]]
        if not (dominant_color[0] == dominant_color[1] == dominant_color[2]):  # Exclude grayscale
            return list(map(int, dominant_color))
    return list(map(int, dominant_color))  # Return the last color if all are grayscale

# Function to find the closest color name
def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

# Function to get color name
def get_color_name(requested_color):
    try:
        closest_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        closest_name = closest_color(requested_color)
    return closest_name

# Streamlit UI
page_bg_img = '''
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
}
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
    width: 700px;
    height: 600px;
    border-radius: 15px;
}
.arrow {
    position: absolute;
    bottom: -10px;
    margin-left: 44px;
    width: 0;
    height: 0;
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-top: 10px solid black; /* Arrow color */
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
.b {
    margin-top: 100px;
    text-align: center;
    font-family: Arial, sans-serif;
    margin-right: 83%;
    color: purple;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown('<h1 class="title">Webcam Color Detection</h1>', unsafe_allow_html=True)

st.markdown('<p class="para">Welcome to our color detection tool, designed with accessibility in mind. We understand that colorblindness can affect the way individuals perceive colors, which is why our tool aims to assist those with color vision deficiencies. With our application, you can accurately identify colors and understand the hues that you may have difficulty distinguishing.</p>', unsafe_allow_html=True)

st.markdown('<img src="https://img.freepik.com/premium-photo/beautiful-colorful-wallpapers-4k_762785-10350.jpg?w=900" class="img" alt="Image">', unsafe_allow_html=True)

st.markdown('<p class="b">Click here to<br> capture the<br> image</p>', unsafe_allow_html=True)
st.markdown('<span class="arrow"></span>', unsafe_allow_html=True)

if st.button('Capture Image'):
    # Capture image from webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
    else:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Could not read frame from webcam.")
            cap.release()
        else:
            # Select Region of Interest (ROI)
            x, y, w, h = cv2.selectROI("Select ROI", frame, fromCenter=False)
            cv2.destroyWindow("Select ROI")

            # Ensure ROI is valid
            if w == 0 or h == 0:
                st.error("Error: Invalid ROI selected.")
            else:
                # Crop the ROI from the frame
                roi = frame[y:y+h, x:x+w]
                # Convert ROI from BGR to RGB
                roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
                # Get dominant color in ROI
                dominant_color = get_dominant_color(roi_rgb)
                st.write("Dominant Color (RGB):", dominant_color)
                # Get color name
                color_name = get_color_name(dominant_color)
                st.write("Color Name:", color_name)
                # Display the captured ROI
                st.image(roi_rgb, channels="RGB")

    if 'cap' in locals():
        cap.release()
    cv2.destroyAllWindows()
