import torch

X = torch.tensor([[1, 2, 3], [4, 5, 6]])

y = X.sum(axis=0)
print(y)

z = X.sum(axis=1)
print(z)
