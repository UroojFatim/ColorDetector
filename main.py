import streamlit as st
import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
import webcolors
from PIL import Image
import io

def get_dominant_color(image, k=3):
    # Convert image from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # Apply KMeans clustering to find the dominant color
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(image)

    # Get the cluster centers and the labels for each pixel
    colors = kmeans.cluster_centers_
    labels = kmeans.labels_

    # Count the number of pixels in each cluster
    label_counts = Counter(labels)
    
    # Find the most common cluster (dominant color)
    dominant_color = colors[label_counts.most_common(1)[0][0]]

    return list(map(int, dominant_color))  # Convert to list of integers

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_color_name(requested_color):
    try:
        closest_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        closest_name = closest_color(requested_color)
    return closest_name

st.title("Webcam Color Detection")

# Capture image from webcam
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    
    # Convert the bytes data to a numpy array
    image = Image.open(io.BytesIO(bytes_data))
    frame = np.array(image)
    
    st.image(frame, caption="Captured Image", use_column_width=True)
    
    # Select Region of Interest (ROI)
    x = st.slider("X", 0, frame.shape[1], 0)
    y = st.slider("Y", 0, frame.shape[0], 0)
    w = st.slider("Width", 1, frame.shape[1] - x, frame.shape[1] - x)
    h = st.slider("Height", 1, frame.shape[0] - y, frame.shape[0] - y)

    # Ensure ROI is valid
    if w > 0 and h > 0:
        # Crop the ROI from the frame
        roi = frame[y:y+h, x:x+w]
        st.image(roi, caption="Selected ROI", use_column_width=True)

        # Get dominant color in ROI
        dominant_color = get_dominant_color(roi)
        st.write("Dominant Color (RGB):", dominant_color)

        # Get color name
        color_name = get_color_name(dominant_color)
        st.write("Color Name:", color_name)
