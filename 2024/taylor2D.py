import numpy as np
import matplotlib.pyplot as plt

x = 0.4
y = 0.4
f = np.sin(x + 2 * y)
f2 = 0 + x + 2 * y
print('f =',f)
print('f2=',f2)
e = np.abs(f-f2) / np.abs(f)
print('e =',e)