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

f = np.linspace(0.1, 1e6, 100)
w = 2 * np.pi * f
V0 = 5

ZC = 1 / (1j * w * C)

VC = ZC / (ZC + R) * V0
VR = R / (ZC + R) * V0

plt.close('all')
plt.plot(f, np.abs(VC), '-rs', label = 'VC')
plt.plot(f, np.abs(VR), '-bo', label = 'VR')
plt.legend()
plt.xlabel('f [Hz]')
plt.ylabel('Voltage [V]')





