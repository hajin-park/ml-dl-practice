import torch

x = torch.arange(20, dtype=torch.int16)
print(x)
y = x.reshape(4, -1)
print(y)
z = y[:, 1]
print(z)
binary_op = y - z.reshape(4, -1)
print(binary_op)
print(binary_op.item())
