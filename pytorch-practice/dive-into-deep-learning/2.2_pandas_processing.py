import torch
import pandas as pd
import os


os.makedirs(os.path.join("..", "..", "data"), exist_ok=True)
data_file = os.path.join("..", "..", "data", "tiny_house.csv")

with open(data_file, "w") as f:
    f.write(
        """NumRooms,RoofType,Price
NA,NA,127500
2,NA,106000
4,Slate,178100
NA,NA,140000"""
    )

data = pd.read_csv(data_file)
# print(data)

# one-hot encoding to for categorical NAN values
inputs, target = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = pd.get_dummies(inputs, dummy_na=True)
# print(inputs)

# mean value of column replaces numerical NAN values
inputs = inputs.fillna(inputs.mean())
# print(inputs)

# convert entries into tensors
X = torch.tensor(inputs.to_numpy(dtype=float))
y = torch.tensor(target.to_numpy(dtype=float))
print(X, y)
