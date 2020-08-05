import numpy as np
import matplotlib.pyplot as plt

'''se graficara y-x para un objeto con y si resistencia del aire'''
import math as m

# se crea una funcion que relacione los valores de 'x' con los de 'y'
def y_val(x,v0):
    theta = 35 * np.pi / 180    # rad
    g = 9.8         # m/s^2      # m/s
    return((x*np.tan(theta)) - ((0.5*g*x**2) / ((v0**2)*(np.cos(theta))**2)))

v0 = 25.63

# se crea un arreglo con las x's a valuar y un arrego de ceros
x = np.linspace(0,63,100)
y = np.zeros(len(x))

# se valua la funcion y se insertan los valores en el arreglo de ceros
for i in range(len(x)):
    y[i] = y_val(x[i] ,v0)

# se crea la una recta horizontal que delimite el suelo
y2 = np.zeros(len(x))

# se crea una recta vertical que delimite la barra
y3 = np.linspace(0,2,100)
x3 = np.zeros(len(y3))
for i in range(len(y3)):
    x3[i] = 60

# se plotean los datos
plt.plot(x3,y3,'-b')
plt.plot(x,y2,'--r')
plt.plot(x,y,'--g',label='Sin Resistencia')


# etiquetas
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica x-y')

from scipy.integrate import solve_ivp


def odeSystem(t, y):
    b = 0.0127627
    x1, y1, x2, y2 = y
    f = [y1,
         -b*y1*np.sqrt(y1**2 + y2**2),
         y2,
         -b*y2*np.sqrt(y1**2 + y2**2) - 9.8]
    return f

t  = np.linspace(0, 10, 1000)

v0 = 35.5

x1 = 0
y1 = v0 * np.cos(35*np.pi/180)
x2 = 0
y2 = v0 * np.sin(35*np.pi/180)

solution = solve_ivp(odeSystem, [0, 10], [x1, y1, x2, y2],
                     t_eval=np.linspace(0, 10, 100))

'''
print(solution.t)
print(solution.y[0])
print(solution.y[1])
print(solution.y[2])
'''

xx = np.zeros(27)
yy = np.zeros(27)

for i in range(27):
    xx[i] = solution.y[0][i]
    yy[i] = solution.y[2][i]

# se ajustan los ejes para no tomar en cuenta los datos de "relleno"
plt.xlim(0,65)
plt.ylim(-1,20)

# se plotean los datos de posicion
plt.plot(solution.y[0], solution.y[2], '-k',label='Resistencia')

# Se muestra la leyenda (los labels en los plots)
plt.legend()

# se guarda y se muestran los datos
plt.savefig('problema6.pdf')
plt.show()
