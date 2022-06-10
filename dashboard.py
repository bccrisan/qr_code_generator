import streamlit as st
import pandas as pd
import numpy as np


def app():
    st.write(''' ### Dashboard page ''')
    text_input = st.number_input("Please input the number of days to plot", value=20, min_value=0, max_value=365)

    rooms = ['Living Room', 'Dorm 1', 'Dorm 2', 'Kitchen']

    chart_data = pd.DataFrame(np.random.rand(text_input, 4), columns=rooms)

    st.line_chart(chart_data)

