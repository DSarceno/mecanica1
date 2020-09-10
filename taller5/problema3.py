# @Author: Diego Sarceno
# Date: 9.09.2020

import numpy as np
import matplotlib.pyplot as plt

# solucion de la parte homogenea
def xh(t,w0,w,beta):
    C1 = 10
    C2 = 2
    lam = np.sqrt(w0**2 - beta**2)
    return np.exp(-beta*t)*(C1*np.cos(lam*t) + C2*np.sin(lam*t))

# constantes de la solucion particular
def A(t,w0,w,beta,a):
    f0 = 2.2
    return ((w0**2 - w**2 + a**2 - 2*beta*a)*f0)/((w0**2 - w**2 + a**2 - \
    2*beta*a)**2 + 4*w**2 * (beta - a)**2)

def B(t,w0,w,beta,a):
    f0 = 2.2
    return (2*w*(beta - a)*f0)/((w0**2 - w**2 + a**2 - 2*beta*a)**2 + \
    4*w**2 * (beta - a)**2)

def xp(t,w0,w,beta,a):
    return np.exp(-a*t)*(A(t,w0,w,beta,a)*np.cos(w*t) + \
    B(t,w0,w,beta,a)*np.sin(w*t))

# Se crean los arreglos
t = np.linspace(0,20,1000)
x = np.zeros(len(t))

for i in range(len(t)):
    x[i] = xh(t[i],2,1,0.1) + xp(t[i],2,1,0.1,0.5)

plt.plot(t,x,'-b',label='$\omega _o = 2$, $\omega = 1$ y $\\beta = 0.1$')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('Posicion')
plt.savefig('problema3_1.pdf')
plt.show()


for i in range(len(t)):
    x[i] = xh(t[i],4,0.1,1) + xp(t[i],4,0.1,1,0.5)

plt.plot(t,x,'-b',label='$\omega _o = 4$, $\omega = 0.1$ y $\\beta = 1$')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('Posicion')
plt.savefig('problema3_2.pdf')
plt.show()


for i in range(len(t)):
    x[i] = xh(t[i],7,5,0.01) + xp(t[i],7,5,0.01,0.5)

plt.plot(t,x,'-b',label='$\omega _o = 7$, $\omega = 5$ y $\\beta = 0.01$')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('Posicion')
plt.savefig('problema3_3.pdf')
plt.show()
