"""
A indexação é feita de forma similar a arrays Numpy, através da sintaxe de colchetes [].
Tensor é uma estrutura mutavel, conseguimos tbm acessar/indexar partes do tensor.
"""
import torch
import numpy as np

tnsr = torch.randn(3, 3)

print(tnsr)
tnsr[0, 2] = -10
print('Modificação aplicada')
print(tnsr)

print('Fatia de tensor')
print(tnsr[0:2])

print('Todos os elementos da coluna 2')
print(tnsr[:, 2])

print('indexando apenas um unico elemento, tensor de dimensão 0')
print(tnsr[0, 2].size())
