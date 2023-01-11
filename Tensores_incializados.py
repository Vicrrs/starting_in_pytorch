"""
Essas funçoes recebem como parâmetro o tamanho de cada dimensão do tensor
* torch.ones() -> cria tensor preenchido com zeros
* torch.zeros() -> cria tensor preenchido com uns.
* torch.randn() -> Cria um tensor preenchido com números aleatórios a partir de uma distribuição normal.
"""
import torch

# lembrar de passar a denmensão do tensor como argumento

tns1 = torch.ones(2, 3)
tns0 = torch.zeros(4, 5)
tnsr = torch.randn(3, 3)

print(tns1)
print(tns0)
print(tnsr)
