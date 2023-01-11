'''
Nossa reta pode ser interpretada como um modelo linear, que nada mais é do que uma função de mapeamento
X -> Y, que mapeia cada ponto em X para um ponto em Y. Em outras palavras, dados os parâmetros W = {w1,w2}
e b de uma reta, é possível mapear uma entrada X = {x1, x2} para a saída f(x; W, b).
Para problemas de classificação, os valores de y para novas entradas x vão definir se x é um ponto acima ou
abaixo da reta, formando portanto um classificador capaz de separar linearmente problemas com duas classes.

#Regra Geral
Formalizando a nomeclatura de redes neurais, em duas dimensões(x1, x2) nosso modelo linear tem dois pesos
(w1, w2) e um viés b, que em inglês são chamados de weight e bias.

Em duas dimensões nosso modelo forma uma reta, como vimos anteriormente. Para um número de dimensões d > 2,
modelos lineares são chamados de hiperplanos, e são compostos por:
    * um peso wi para cada dimensão xi
    * um único viés b
Exemplo, para 3 dimensões (x1, x2, x3) teríamos 3 pesos (w1, w2, w3) e um único viés b. Sua função de mapea-
mento seria y = w1x1 + w2x2 + w3x3 + b

De forma geral, define-se que dada uma entrada com d dimensões, a função de mapeamento de um modelo linear é:

y = \sum_{i=1}^{d} wi.xi + b
'''
#Exercício de Classificação Linear
"""
Vamos treinar um classificador linear em duas dimensões usando a tecnologia mais avançada que existe: o cérebro
A célula a seguir produz uma distribuição aleatória para um problema de classificação com duas classes, usando
a função make_classification() do sklearn.
"""
import torch
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

#Fixando a aleatorização dos dados, definimos uma raiz para isso
np.random.seed(46)

X, Y = make_classification(n_features=2, n_redundant=0, n_informative=1,
                            n_clusters_per_class=1)

#Gera retas entre os pontos
#plt.plot(X[:, 0], X[:, 1], marker = 'o')

#plotando apenas os pontos, espalhamento de dados
plt.scatter(X[:, 0], X[:, 1], marker = 'o', c =Y,
            edgecolor='k')
#plotando um dos pontos dos dados
p = X[10]
print(Y[10])
plt.plot(p[0], p[1], marker='^', markersize=20)

plt.show()