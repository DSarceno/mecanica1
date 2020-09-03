# @Author: Diego Sarceno
# Date: 2.09.2020

import matplotlib.pyplot as plt
import numpy as np
import math as m

# SE DEFINE UNA FUNCION DE POSICION
def x(t):
    # CONSTANTES
    Ao = 5
    beta = 0.1
    wo = 1
    w1 = m.sqrt(wo**2 - beta**2)
    return Ao*m.exp(-beta*t)*m.cos(w1*t)

# SE CREAN ARRELGOS
t = np.linspace(0,50,100)
r = np.zeros(len(t))

# SE VALUA LA FUNCION
for i in range(len(t)):
    r[i] = x(t[i])

# SE PLOTEA
plt.plot(t,r,'-k',label='$x(t)$')
plt.legend()
plt.xlabel('Tiempo')
plt.ylabel('Posicion')
plt.title('Problema 5')
plt.savefig('problema5.pdf')
plt.show()
