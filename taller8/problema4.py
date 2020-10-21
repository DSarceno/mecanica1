#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: Diego Sarceno
# Date: 20.10.2020


from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# se crea el sistema de EDs a resolver
def system(t, y):
    # constantes (algo exageradas jeje)
    q = 10
    E0 = 20
    c = 1
    B0 = 50
    m = 60
    x1, y1, x2, y2 = y
    f = [y1,
        q*(E0*np.sin(((q*B0)/(m*c))*t) + y2*B0),
        y2,
        -(B0/m)*y1]
    return f
# condiciones iniciales
x1 = 0
y1 = 0
x2 = 0
y2 = 0

# se resuelve el sistema de EDs con CI
sol = solve_ivp(system,[0,10],[x1,y1,x2,y2],t_eval = np.linspace(0,10,10000))

# se grafica y se añaden detalles chingones
plt.plot(sol.y[0],sol.y[2],'-k',label='Trayectoria')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Trayectoria de la Partícula')
plt.legend()
plt.savefig('problema4.pdf')
plt.show()
