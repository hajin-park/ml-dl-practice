import math
import time
import numpy as np
import torch
from d2l import torch as d2l
import matplotlib.pyplot as plt

"""
Vectorization for speed comparison example
"""
# n = 10_000
# a = torch.ones(n)
# b = torch.ones(n)

# c = torch.zeros(n)
# t = time.time()

# for i in range(n):
#     c[i] = a[i] + b[i]
# print(f"{time.time() - t:.5f} seconds")

# t = time.time()
# d = a + b
# print(f"{time.time() - t:.40f} seconds")


def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma**2)
    return p * np.exp(-0.5 / sigma**2 * (x - mu) ** 2)


x = np.arange(-7, 7, 0.1)

params = [(0, 1), (0, 2), (3, 1)]

d2l.plot(
    x,
    [normal(x, mu, sigma) for mu, sigma in params],
    xlabel="x",
    ylabel="p(x)",
    figsize=(4.5, 2.5),
    legend=[f"mean {mu}, std {sigma}" for mu, sigma in params],
)
plt.show()
