import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x - y

density = 40

x = np.linspace(-5, 5, density)
y = np.linspace(-5, 5, density)

X, Y = np.meshgrid(x, y)

DY = f(X, Y)
DX = np.ones_like(DY)

magnitude = np.sqrt(DX**2 + DY**2)
DX = DX / magnitude
DY = DY / magnitude

plt.figure(figsize=(6, 6))
plt.quiver(X, Y, DX, DY)
plt.show()