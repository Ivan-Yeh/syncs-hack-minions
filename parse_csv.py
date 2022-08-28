from pages.space import Space
import pandas as pd
import os
import plotly.express as px

def main():
    space_ls = []

    files = os.listdir("data_files/",)
    for file in files:
        if file[-4:] == ".csv":
            file_df = pd.read_csv("./data_files/abs.csv")
            for i in range(0, len(file_df)):
                space_ls.append(Space(file.replace(".csv", "").replace("data_files/", "").upper(), file_df.iloc[i]))
    
    return space_ls, file_df
 
# for space in space_ls:
#     print(space.building_name)