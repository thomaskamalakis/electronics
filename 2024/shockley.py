import numpy as np
import matplotlib.pyplot as plt

IS = 1e-12
VT = 26e-3
n = 1.5

vD = np.linspace(0.8, 0.9, 1000)
i = IS * ( np.exp(vD / (n*VT)) - 1 )


VC = 0.85
IC = IS * ( np.exp(VC / (n*VT)) - 1 )

i_deriv = IS / (n * VT) * np.exp(VC/ (n*VT) )
Dv = vD - VC
Di = i_deriv * Dv

i2 = IC + Di

plt.close('all')
plt.plot(vD, i*1e3, label = 'Exponential')
plt.plot(vD, i2*1e3, label = 'Small signal approximation')

plt.ylabel('I [A]')
plt.xlabel('V [Vt]')
plt.legend()

error = 100 * np.abs(i - i2) / np.abs(i)
plt.figure()
plt.plot(vD, error)
plt.ylabel('Error [%]')



 
 