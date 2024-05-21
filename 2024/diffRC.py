import numpy as np
import matplotlib.pyplot as plt

R = 1e4
C = 1e-9
    
T0 = 1e-4
Tmax = 2 * T0
t = np.linspace(0, Tmax, 10000)
m = np.mod(t, T0)
plt.close('all')
v = (m>T0/2)
plt.plot(t, v)

Dt = t[1] - t[0]
vC = np.zeros(t.size)

for i, t1 in enumerate(t):
    if i < t.size-1:
        print(i)
        vC[i+1] = vC[i] + Dt/(R * C) * (v[i] - vC[i])
        
plt.close('all')
plt.plot(t, v, label='v')
plt.plot(t, vC, label='vC')
plt.legend()