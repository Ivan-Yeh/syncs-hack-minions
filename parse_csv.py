from space import Space
import pandas as pd
import os
import plotly.express as px

space_ls = []

# files = os.listdir("data_files")
# for file in files:
file = "data_files/abs.csv"
file_df = pd.read_csv("data_files/abs.csv")
for i in range(0, len(file_df)):
    space_ls.append(Space(file.replace(".csv", "").replace("data_files/", "").upper(), file_df.iloc[i]))
        
        
for space in space_ls:
    print(space.visitor_dist)
    px.histogram(space.visitor_dist, x = "time", y = "visitors").show()