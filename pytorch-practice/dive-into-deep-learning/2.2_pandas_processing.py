import torch
import pandas as pd
import os


os.makedirs(os.path.join("..", "data"), exist_ok=True)
data_file = os.path.join("..", "data", "tiny_house.csv")

with open(data_file, "w") as f:
    f.write(
        """ NumRooms,RoofType,Price
            NA,NA,127500
            2,NA,106000
            4,Slate,178100
            NA,NA,140000"""
    )

data = pd.read_csv(data_file)
print(data)
