import streamlit as st


def app():
    st.write(''' # Homepage ''')

    try:
        with open("README.md") as file:
            body = file.read()
    except:
        print("Error opening file")

    st.markdown(body, unsafe_allow_html=False)
