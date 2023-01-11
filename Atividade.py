import torch
from torch import nn

## Resumo do Código com o módulo nn.Sequential
net_sequential = nn.Sequential(
    nn.Linear(in_features=3, out_features=6),
    nn.ReLU(),
    nn.Linear(in_features=6, out_features=3)
)


## Resumo do código com o nn.Module
class Net(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):
        super(Net, self).__init__()

        # Definir a arquitetura
        self.hidden = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.output = nn.Linear(hidden_size, output_size)

    def forward(self, X):
        # Gerar uma saída a partir do X
        hidden = self.relu(self.hidden(X))
        output = self.output(hidden)

        return output


net_module = Net(input_size=3, hidden_size=6, output_size=3)
