import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt



def f(t,r):
    x, y = r
    fx = np.cos(y)
    fy = np.sin(x)
    return(fx, fy)

sol = integrate.solve_ivp(f, (0,10), (1,1), t_eval = np.linspace(0,10,100000))
x, y = sol.y
plt.plot(x,y)
plt.axis('scaled')
plt.show()


# se definen las constantes a considerar
m = 0.2
cW = 0.5
rho = 1.3
theta = 35
A = np.pi * 005**2


# se define la funcion que contiene el sistema de ED's
def f(t,vr):
    vx, vy = vr
    fx1 = -(0.5*cW*rho*A/m)
