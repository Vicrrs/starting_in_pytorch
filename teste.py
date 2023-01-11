import torch

tns = torch.randn(9, 12)
tns1 = tns[0:5, 0:4]
tns2 = tns[5:, 4:]

resultado = torch.mm(tns1, tns2)
print(resultado.size())
