import numpy as np
import matplotlib.pyplot as plt

'''se graficara y-x para un objeto con y si resistencia del aire'''
import math as m

# se crea una funcion que relacione los valores de 'x' con los de 'y'
def y_val(x):
    theta = (7 / 36)*m.pi       # rad
    g = 9.8         # m/s^2
    v0 = 25.63      # m/s
    return((x*m.tan(theta)) - ((0.5*g*x**2) / ((v0**2)*(m.cos(theta))**2)))

# se crea un arreglo con las x's a valuar y un arrego de ceros
x = np.linspace(0,63,100)
y = np.zeros(len(x))

# se crea la una recta horizontal que delimite el suelo
y2 = np.zeros(len(x))

# se crea una recta vertical que delimite la barra
y3 = np.linspace(0,2,100)
x3 = np.zeros(len(y3))
for i in range(len(y3)):
    x3[i] = 60

# se valua la funcion y se insertan los valores en el arreglo de ceros
for i in range(len(x)):
    y[i] = y_val(x[i])

# se plotean los datos
plt.plot(x3,y3,'-b')
plt.plot(x,y2,'--r')
plt.plot(x,y,'--k')

# etiquetas
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica x-y')

plt.show()
