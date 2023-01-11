import torch
from torch import nn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

torch.manual_seed(46)
perceptron = nn.Linear(in_features=3, out_features=1)


def plot3d(perceptron):
    w1, w2, w3 = perceptron.weight.data.numpy()[0]
    bias = perceptron.bias.data.numpy()

    X1 = np.linspace(-1, 1, 10)
    X2 = np.linspace(-1, 1, 10)

    X1, X2 = np.meshgrid(X1, X2)
    X3 = (bias - w1 * X1 - w2 * X2) / w3

    fig = plt.figure(figsize=(10, 8))
    ax = fig.gca(projection='3d')

    ax.plot_surface(X1, X2, X3, cmap='plasma')
    X = torch.Tensor([0, 1, 2])
    y = perceptron(X)
    plt.plot([X[0]], [X[1]], [X[2]], color='r', marker='^', markersize=20)
    plt.show()


plot3d(perceptron)

