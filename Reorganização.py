"""
Função .size() e .view()

Uma operação importantíssima na manipulação de tensores para Deep Learning é a reorganização das suas dimensões. Dessa
forma podemos, por exemplo, linearizar um tensor n-dimensional
"""

import torch

tnsr = torch.randn(2, 2, 3)

print(tnsr)
print(tnsr.size())

print('')
# Usando o .view() para redimensionar esse tensor
tns = tnsr.view(12)
print(tns)