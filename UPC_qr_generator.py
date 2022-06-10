import numpy as np
import pandas as pd
import streamlit as st

store970upcs = [
    [194133406850, "Girls Overalls", "Price", "4", "Pink"],
    [194133406850, "Girls Overalls", "Price", "4", "Pink"],
]


def app():
    st.write(''' # List of UPCs for store #970 ''')
    df = pd.DataFrame(store970upcs, columns=("UPC", "Name", "Price", "Size", "Colour"))
    st.table(df)

