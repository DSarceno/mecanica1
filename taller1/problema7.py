from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

'''utilizando lo encontrado en el problema 7 del taller 1
se toman las ecuaciones que modelan el movimiento de la masa'''

# CONSTANTES:
z0 = 20
phi_o = 0       # desfase
omega = 3
vz0 = 6
g = 9.8
R = 5

# R3
fig = plt.figure()
ax = fig.gca(projection='3d')

# PARAMETRO TEMPORAL
t = np.linspace(0,3.5,1000)

# PARAMETRIZACION EN COORDENADAS CARTESIANAS
x = R * np.cos((omega * t) + phi_o)
y = R * np.sin((omega * t) + phi_o)
z = vz0 * t

# GRAFICA
ax.plot(x,y,z,'-k')

# MODIFICACION DE EJES Y ANGULO DE VISTA
ax.set_zlim(0,20)
ax.view_init(30,30)

# CAPTIONS DE LOS EJES
ax.set_xlabel('x(t)')
ax.set_ylabel('y(t)')
ax.set_zlabel('z(t)')
ax.set_title('Problema 7')

# NUMERACION DE LOS EJES
ax.set_xticks([0])
ax.set_yticks([0])
ax.set_zticks([0])


# MUESTRA Y GUARDA
plt.savefig('problema7.pdf')
plt.show()
