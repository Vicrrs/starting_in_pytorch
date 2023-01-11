# Solucionando a equação da reta para diferentes pontos
# Reta: -1x + 4x + 0.4
# ax + by + c = 0
# y = (-a*x - c)/b
# A reta é um classificador
"""
Note queoponto p₁ está na reta,enquanto p₂ está acima da retaep3 abaixo.Ao solucionaraequação da reta para esses três
pontos,tivemos respectivamente resultados nulo(=0),positivo(>0)e negativo(<0).
Esse comportamentoéconsistente para quaisquer pontos na reta,acima ou abaixo dela.Ou seja,se chamarmosaequação da
reta def(x),temos as seguintes regras:
   f(x)=0define pontos na reta
   f(x)>0define pontos acima da reta
   f(x)<0define pontos abaixo da reta
"""

from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

a = -1
b = 4
c = 0.4

def plotline(a, b, c):
    x = np.linspace(-2, 4, 50)
    p1 = (2, 0.4)
    p2 = (1, 0.6)
    p3 = (3, -0.4)
    ret1 = a*p1[0] + b*p1[1] + c
    y = (-a * x - c) / b
    plt.axvline(0, -1, 1, color='k', linewidth=1)
    plt.axhline(0, -2, 4, color='k', linewidth=1)
    plt.plot(x, y)
    plt.plot(p1[0], p1[1], color='b', marker ='o' )
    plt.plot(p2[0], p2[1], color='r', marker ='o' )
    plt.plot(p3[0], p3[1], color='g', marker ='o' )
    plt.grid(True)
    plt.show()
plotline(a, b, c)
