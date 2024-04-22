import numpy as np
from costFunctions import costFunction
import matplotlib.pyplot as plt


@np.vectorize
def deJong5(x1, x2):
    a1 = [-32.0, -16.0, 0.0, 16.0, 32.0]*5
    a2 = [-32.0]*5 + [-16.0]*5 + [0.0]*5 + [16.0]*5 + [32.0]*5
    a = [a1, a2]

    sum = 0.002
    for i in range(1, 26):
        sum += ( 1 / (i + (x1 - a[0][i-1])**6 + (x2 - a[1][i-1])**6) )
    
    return 1.0/sum



X, Y = np.meshgrid(np.linspace(-65.536, 65.536, 100), np.linspace(-65.536, 65.536, 100))
Z = deJong5(X, Y)

plt.imshow(Z, extent=(X.min(), X.max(), Y.max(), Y.min()), interpolation='nearest')

plt.show()
"""
z = []
for i in range(len(x)):
    z.append(costFunction((x, y)))

z = np.array(z)

#grid = z.reshape((len(x), len(y)))

plt.imshow(z, extent = (x.min(), x.max(), y.max(), y.min()), interpolation='nearest')

plt.show()
"""