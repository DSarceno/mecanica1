import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


'''Del ejercicio 1 del taller, se toma la trayectoria de la particula
y se representa en una grafica 3d'''

# Se definen las constantes
b = 4
c = 9
omega = 3
v0 = 2.5

# para que los ejes no se ajusten automaticamente
max = np.maximum(b+4,c+4)
xmin = -max
ymin = -max
xmax = max
ymax = max

# se genera R3
fig = plt.figure()
ax = fig.gca(projection='3d')

# se genera el rango de t y se valuan las funciones
t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
x = b * np.cos(omega * t)
y = c * np.sin(omega * t)
z = v0 * t


# se grafica la curva parametrica
ax.plot(x, y, z, '-k')

# mantiene los ejes fijos, sin ajustarse automáticamente
#ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
ax.set_zlim(-20,20)

# Para modificar el angulo de la grafica
#ax.view_init(30, 30)

# Guarda el archivo o lo muestra
plt.savefig('problema1.pdf')
#plt.show()
