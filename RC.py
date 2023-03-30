import numpy as np
import matplotlib.pyplot as plt

ta = -1e-6
tb = 2e-6
N = 20000
V0 = 1
R = 1e3
C = 1e-11
a = 1 / (R * C)

t = np.linspace(ta, tb, N)
Dt = t[2] - t[1]
T1 = 1e-6
vIN = np.zeros(N)
j = np.where( (t>-T1/2) & (t <= T1/2 ) )
vIN[j] = V0
plt.figure(1)
plt.plot(t, vIN)

vC = np.zeros(N)
for i in range(vC.size):
    if i > 1:
        vC[i] = vC[i-1] + a * Dt * (vIN[i-1] - vC[i-1])
    
plt.figure(2)
plt.plot(t, vIN, t, vC)

    




