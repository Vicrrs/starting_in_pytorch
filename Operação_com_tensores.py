# Operação com Tensores
"""
A função .item() utilizada extrai o número de um tensor que possui um único valor, permitindo realizar operações numéric
as do Python. Caso o item nao seja extraído, operações que envolvam tensores vaão retornar novos tensores.

Operações com tensores são realizadas ponto a ponto, operando cada elemento (i, j) do tensor t1, com elemento (i, j) do
tensor t2.
"""
import torch

tnsr = torch.randn(3, 3)
tnsr1 = torch.randn(3, 3)

print(tnsr)
print(tnsr1)

print(tnsr + tnsr1)
# multiplica ponto a ponto
print(tnsr * tnsr1)
print(tnsr / tnsr1)

# Para fazer produto interno nas matrizes usamos
print(torch.mm(tnsr, tnsr1))

