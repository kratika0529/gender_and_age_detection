import streamlit as st
import cv2
import numpy as np
from PIL import Image
from detect import detect_gender_and_age  # You will need to define this

st.title("🧠 Gender and Age Detection")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, channels="BGR", caption="Uploaded Image", use_column_width=True)
    
    gender, age = detect_gender_and_age(image)  # ← You define this in detect.py
    st.markdown(f"**Predicted Gender:** {gender}")
    st.markdown(f"**Predicted Age:** {age}")
