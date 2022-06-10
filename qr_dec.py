import streamlit as st
import cv2
import os
from PIL import Image


def app():
    st.write(''' # QR Code Decoder ''')
    st.write(' A Web App That Decods Your QR Codes. ')

    file = st.file_uploader("Please Upload The Image of QR Code", type=['jpg', 'png'])
    if file is None:
        st.text("Please upload an image file..")
    else:
        image = Image.open(file)
        image.save("qr.png")
        st.image(image, use_column_width=True)
        img = cv2.imread('qr.png')
        det = cv2.QRCodeDetector()
        val = det.detectAndDecode(img)
        st.write(f"Decoded Message: {val[0]}")
        os.remove("qr.png")
