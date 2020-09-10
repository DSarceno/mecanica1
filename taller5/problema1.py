# @Author: Diego Sarceno
# Date: 9.09.2020

import numpy as np
import matplotlib.pyplot as plt

def GS_WD(t,F0):
    '''Constantes:'''
    beta = 0.1
    w0 = 1
    k = 2
    lam = np.sqrt(w0**2 - beta**2)
    C1 = 10
    C2 = 0.1
    return np.exp(-beta*t)*(C1*np.cos(lam*t) + C2*np.sin(lam*t)) + F0/k

# SE CREAN LOS ARREGLOS DONDE SE GUARDARAN LOS VALORES A PLOTEAR
t = np.linspace(0,50,1000)
x = np.zeros(len(t))
x_F0 = np.zeros(len(t))

# SE VALUA LA FUNCION PARA F0 = 0 Y UN VALOR ARBITRARIO
for i in range(len(t)):
    x[i] = GS_WD(t[i],0)
    x_F0[i] = GS_WD(t[i],2.2)

# SE PLOTEAR
plt.plot(t,x,'-b',label='$F_o = 0$')
plt.plot(t,x_F0,'-g',label='$F_o = 2.2N$')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('Oscilaciones Infraamortiguadas')
plt.savefig('problema1.pdf')
plt.show()
