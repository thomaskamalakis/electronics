import numpy as np
import matplotlib.pyplot as plt

N = 20000
f = 1e6
V0 = 1
R = 1e3
C = 1e-10
a = 1 / (R * C)
ta = 0e-6
tb = 10e-6
t = np.linspace(ta, tb, N)
Dt = t[2] - t[1]


vIN = np.sin(2 * np.pi * f * t)

plt.figure(1)
plt.plot(t, vIN)

vC = np.zeros(N)
for i in range(vC.size):
    if i > 1:
        vC[i] = vC[i-1] + a * Dt * (vIN[i-1] - vC[i-1])
    
plt.figure(2)
plt.plot(t, vIN, t, vC)
    
w = 2*np.pi * f
Z = 1 / (1j * w * R * C + 1)
phi = np.angle(Z)
phi_degrees = 180 * phi / np.pi 



