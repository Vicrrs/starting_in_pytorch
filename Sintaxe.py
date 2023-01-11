"""
Pytorch é uma biblioteca de processamento vetorial/matricial/tensorial. Operações com tensores do Pytorch posssuem sinta
xe consideravelmente parecida com operações de tensores do NumPy.

Podemos converter listas comuns do Python em tensores do Pytorch.

Note que a impressão de tensores dos tipos float32 e int64 ão vêm acompanhada do parâmetro de tipo dtype, visto que trat
am de padrões trabalhados pelo PyTorch
"""
import torch

lista = [[1, 2, 3],
         [4, 5, 6]]

#Tipo Float32
tns = torch.Tensor(lista)
print(tns.dtype)
print(tns)

#Convertendo de forma explicita
tns = torch.FloatTensor(lista)
print(tns.dtype)
print(tns)

#Ponto flutuante com maior precisão
tns = torch.DoubleTensor(lista)
print(tns.dtype)
print(tns)

#números interios
tns = torch.LongTensor(lista)
print(tns.dtype)
print(tns)
