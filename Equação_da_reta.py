# Reta: -1x + 4x + 0.4
# ax + by + c = 0
# y = (-a*x - c)/b
import matplotlib.pyplot as plt
import numpy as np

a = -1
b = 4
c = 0.4

# Fixando X
def plotline(a, b, c):
    x = np.linspace(-2, 4, 50)
    y = (-a * x - c) / b

    plt.axvline(0, -1, 1, color='k', linewidth=1)
    plt.axhline(0, -2, 4, color='k', linewidth=1)
    plt.plot(x, y)
    plt.grid(True)
    plt.show()

plotline(a, b, c)
