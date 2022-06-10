import streamlit as st
import qrcode
import os


def app():
    st.write(''' # QR Code Generator ''')
    st.write(' A Web App That Generates QR Code')
    text = st.text_input("Enter Some Text...")
    if text != "":
        qr = qrcode.make(text)
        qr.save(f"{text}.png")
        st.image(f"{text}.png", use_column_width=True)
        os.remove(f"{text}.png")
