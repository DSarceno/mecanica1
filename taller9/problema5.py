#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Diego Sarceno
# Date: 20.10.2020
#
#
#

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

L = 10
g = 9.8

def cadena(t, y):
    x1, v1 = y
    f = [v1,
        (((2*L*x1 - x1**2)/(L - x1))*g)**2]
    return f

x0 = 1E-16
v0 = 0
sol = solve_ivp(cadena,[0,20],[x0,v0],t_eval = np.linspace(0,20,10000))



plt.plot(sol.t,sol.y[0],'-k',label = '$\\dot{x} = \\sqrt{\\frac{2Lx - x^2}{L-x} g}$')
plt.xlabel('$t$')
plt.ylabel('$x$')
plt.legend()
plt.title('Solución a la ED')
plt.savefig('problema5_1.pdf')
plt.show()

c = (2*g*L)**(1/2)
tc = [i/c for i in sol.t]
vc = [i/c for i in sol.y[1]]

plt.plot(tc,vc,'-k')
plt.xlabel('$\\frac{t}{\\sqrt{2gL}}$')
plt.ylabel('$\\frac{\\dot{x}}{\\sqrt{2gL}}$')
plt.title('Velocidad contra tiempo')
plt.savefig('problema5_2.pdf')
plt.show()
