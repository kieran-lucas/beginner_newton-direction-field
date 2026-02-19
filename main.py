import numpy as np

x = np.linspace(-2, 2, 3)
y = np.linspace(-2, 2, 3)

X, Y = np.meshgrid(x, y)

Z = X - Y

print("X =\n", X)
print("Y =\n", Y)
print("Z =\n", Z)
