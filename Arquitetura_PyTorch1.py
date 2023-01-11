"""
A forma mais organizada de definir modelos em PyTorch é implementando uma classe nos moldes da classe nn.Module. Para
redes pequenas, como as que estamos aprendendo até o momento, sua importância pode não se destacar, mas modelos maiores
e com funcionalidades mais complexas, são mais fáceis de implementar e realizar manutenções dessa forma.

Funções obrigatórias do nn.Module.

__init()__: definição de hiperparâmetros e instância do modelo
forward(): Fluxo da entrada para produzir uma saída

"""
import torch
from torch import nn
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

X1, Y1 = make_moons(n_samples=300, noise=0.2)
plt.scatter(X1[:, 0], X1[:, 1], marker='o',
            c=Y1, s=25, edgecolor='k')


class MinhaRede(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):
        super(MinhaRede, self).__init__()

        # Definir a arquitetura
        self.hidden = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.output = nn.Linear(hidden_size, output_size)

    def forward(self, X):
        # Gerar uma saída a partir do X
        hidden = self.relu(self.hidden(X))
        output = self.output(hidden)

        return output


input_size = 2
hidden_size = 8
output_size = 1

net = MinhaRede(input_size, hidden_size, output_size)  ## O método __init__()
print(net)
print("-=-=" * 10)
if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

print(device)
print("-=-=" * 10)
input_size = 2
hidden_size = 8
output_size = 1

net = MinhaRede(input_size, hidden_size, output_size)  ## O método __init__()
net = net.to(device)
print(net)

print("-=-=" * 10)

print(X1.shape)
tensor = torch.from_numpy(X1).float()
tensor = tensor.to(device)
pred = net(tensor)
print(pred.size())
