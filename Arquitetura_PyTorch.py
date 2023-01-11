from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import torch
from torch import nn # neural networks


X1, Y1 = make_moons(n_samples=300, noise=0.2)
plt.scatter(X1[:, 0], X1[:, 1], marker='o',
            c=Y1, s=25, edgecolor='k')

"""
O módulo nn.Sequential é um container onde se pode colocar múltiplos módulos. Ao realizar um forward em um objeto 
Sequential ele aplicará sequencialmente os módulos nele contidas para gerar uma saída.

Segue abaixo um exemplo desse módulo contendo 2 camadas Linear intercaladas por uma função de ativação ReLU.
"""
input_size = 2
hidden_size = 8
output_size = 1

net = nn.Sequential(nn.Linear(in_features=input_size, out_features=hidden_size), # hidden (escondida)
                    nn.ReLU(),   # ativação não linear
                    nn.Linear(in_features=hidden_size, out_features=output_size)) # output (saída)
print(net)

"""
O módulo summary da biblioteca torchsummary nos permite visualizar mais informações sobre a nossa rede, como quantidade 
de parâmetros e o tamanho que cada elemento ocupa na memória.
"""

