import home
import qr_gen
import qr_dec
import dashboard
import UPC_qr_generator
import streamlit as st


PAGES = {
    "Home": home,
    "Generate QR Code": qr_gen,
    "Decods QR Code": qr_dec,
    "Dashboard Page": dashboard,
    "UPCs List": UPC_qr_generator
}


if __name__ == '__main__':
    st.set_page_config(layout='wide')
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Choose Any", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

