#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:10:15 2024

@author: thkam
"""
import numpy as np
import matplotlib.pyplot as plt

V = 5
R1 = 1000
R2 = np.arange(100, 10000, 100)

i = V / (R1+R2)
V1 = i * R1
V2 = i * R2

plt.close('all')
plt.figure()
plt.plot(R2, V2, '-ro', label = 'V2')
plt.plot(R2, V1, '-bs', label = 'V1')
plt.plot(R2,V1+V2,'m--')
plt.legend()
plt.xlabel('R2')
plt.ylabel('Voltage')





