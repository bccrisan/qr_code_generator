import pandas as pd
import streamlit as st
from barcode import EAN13


def app():
    st.write(''' # List of UPCs for store #970 ''')
    col = st.columns(6)
    generate_barcodes()
    with open("updated_data.csv") as data:
        for line in data:
            line_list = line.split(",")
            col[0].write(line_list[0])
            col[1].write(line_list[1])
            col[2].write(line_list[2])
            col[3].write(line_list[3])
            col[4].write(line_list[4])
            if line_list[5] == "Barcode\n":
                col[5].write(line_list[5])
            else:
                col[5].image(line_list[5].split("\n")[0])


def generate_barcodes():
    with open("updated_data.csv", "w+") as out_file:
        with open("data.csv") as in_file:
            for line in in_file:
                line_list = line.split(",")
                if line_list[5] == "\n":
                    new_barcode = EAN13(line_list[0])
                    new_barcode.save(line_list[0])
                    line_list[5] = line_list[0] + ".svg\n"
                result = ",".join(line_list)
                out_file.write(result)
    df = pd.read_csv("updated_data.csv")
    print(df)

