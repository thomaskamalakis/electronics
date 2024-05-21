#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:10:15 2024

@author: thkam
"""
import numpy as np
import matplotlib.pyplot as plt

C = 1e-9
R = 1e3
f = 500e3
t = np.linspace(0, 4/f, 1000)
V0 = 5

V = V0 * np.cos(2*np.pi*f*t)

ZC_A = 1/(1j * 2 * np.pi * f * C)
VA = V0/2 * np.exp(1j * 2 * np.pi * f * t)
vC_A = ZC_A / (ZC_A + R) * VA

ZC_B = 1/(-1j * 2 * np.pi * f * C)
VB = V0/2 * np.exp(- 1j * 2 * np.pi * f * t)
vC_B = ZC_B / (ZC_B + R) * VB

vC = vC_A + vC_B

plt.close('all')
plt.plot(t, V, label = 'input')
plt.plot(t, np.real(vC), label = 'output [C] (Real)')
plt.plot(t, np.imag(vC), label = 'output [C] (Imag)')

plt.xlabel('t [s]')
plt.ylabel('Voltage [V]')
plt.legend()





