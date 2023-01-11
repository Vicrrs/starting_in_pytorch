# Criando Tensores a partir de um array numpy
"torch.from_numpy()"
import numpy as np
import torch

# Criando um array aleatório
arr = np.random.rand(3, 4)

# Convertendo o array pro tipo inteiro
# arr = arr.astype(int)

# convertendo para tensor
tns = torch.from_numpy(arr)

print(arr)
print(arr.dtype)
print(tns)
print(tns.dtype)