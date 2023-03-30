import numpy as np
import matplotlib.pyplot as plt

def find_zero(a, b, f, e = 1e-14):
    
    c = (a+b)/2
    
    while np.abs( f(c) ) > e:
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a+b)/2
    
    return c
    
class diode:
    
    def __init__(self, n = 1.5,
                       VT = 0.025,
                       IS = 1e-10):
    
        self.n = n
        self.VT = VT
        self.IS = IS
        
    def law(self, vD):
        n = self.n
        VT = self.VT
        IS = self.IS
        return IS * ( np.exp(vD /( n * VT ) ) - 1 )

class RD_circuit:
    
    def __init__(self, n = 1.5,
                       VT = 0.025,
                       IS = 1e-10,
                       R = 50):
    
        self.D = diode(n = n, VT = VT, IS = IS)
        self.R = 50
        
    def find_op(self, VB, va = 0, vb = 0.8):
        print(va)
        print(vb)
        f = lambda v : self.D.law(v) - (VB-v) / R
        v0 = find_zero(va, vb, f)
        i0 = self.D.law(v0)
        return i0, v0


D = diode()
vD = np.linspace(-2, 0.75, 1000)
i = D.law(vD)

VB = -1
R = 50

i2 = (VB - vD)/R
 
plt.close('all')
plt.plot(vD, i/1e-3, label = 'D')
plt.plot(vD, i2/1e-3, label = 'Ohm Law')
plt.xlabel('vD [Vt]')
plt.ylabel('i [mA]')
plt.legend()

plt.figure(2)
plt.plot(vD, i2-i)
plt.grid()

RD = RD_circuit()
f0 = 50
T0 = 1/f0
t = np.linspace(0, 3*T0, 100)
VB = 2 * np.sin(2 * np.pi * f0 * t)
#VB = np.array([0])
plt.close('all')
#plt.plot(t, VB)

i0s = np.zeros(VB.size)
v0s = np.zeros(VB.size)

i = 0
for vbv in VB:
    i0, v0 = RD.find_op(vbv, va = np.min([vbv, -0.1]), vb = 0.8)
    i0s[i] = i0
    v0s[i] = v0
    i += 1

vR = VB - v0s
plt.figure()
plt.plot(t, VB, label = 'input')
plt.plot(t, v0s, '-.', label = 'diode')
plt.plot(t, vR, label = 'resistance')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('V [Vt]')

