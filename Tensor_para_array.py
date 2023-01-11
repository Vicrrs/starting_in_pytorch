# Tensor para array numpy

import torch
import numpy as np

tnsr = torch.randn(3, 3)
arr = tnsr.data.numpy()

print(arr)
print(type(tnsr))
print(type(arr))
