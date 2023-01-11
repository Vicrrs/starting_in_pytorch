# GPU CAST

"""
Para que o seus script suporte a infraestrutura com e sem GPU, é importante definir o dispositivo de inicío do seu código
de acordo com uma determinada verificação. Essa definição de dispositivo será utilizada toda vez qure precisamos subir
valores na GPU, com os pesos da rede, os gradientes
"""
import torch

tns = torch.randn(10)

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')
print(device)

# Jogando as informações para GPU

tns = tns.to(device)
print(tns)

