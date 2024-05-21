import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 0.05, 100)
f = np.exp(x)
f2 = 1 + x #+ x ** 2 / 2 + x**3 / np.math.factorial(3) +x**4 / np.math.factorial(4)

plt.close('all')
plt.plot(x, f, label = 'exp')
plt.plot(x, f2, '--', label = 'taylor')
plt.legend()
plt.xlabel('x')
plt.ylabel('f')

    