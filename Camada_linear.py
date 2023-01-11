#CAMADA_LINEAR

from torch import nn #neural networks

#Instanciando um perceptron de camada simples

perceptron = nn.Linear(in_features=3, out_features=1)
print(perceptron)

print('')

#Os pesos W e o viés b são inicializados aleatoriamente pelo PyTorch. Conseguimos consultalos usando:
for nome, tensor in perceptron.named_parameters():
    print(nome, tensor)

print('')

#Também conseguimos consultalos individualmente a partir da camada
print(perceptron.weight.data)
print(perceptron.bias.data)
