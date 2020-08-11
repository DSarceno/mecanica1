
import numpy as np
import matplotlib.pyplot as plt

'''Este programa creara una grafíca del potencial
encontrado en el ejercicio 6 del taller 2'''

# se crea una funcion que represente el potencial
def V(x):
	a = 2
	k = 3
	return 0.5*(k*x**2 + a/x**2)

# se crea un arreglo con los valores a valuar de x
x = np.linspace(-10,10,100)

# se crea otro arreglo de ceros
y = np.zeros(len(x))

# se valua la funcion y se agrega al arreglo de ceros
for i in range(len(x)):
	y[i] = V(x[i])

# se plotean los datos obtenidos
plt.plot(x,y,'-k',label='$V(x)$')

# se agregan los labels y la leyenda
plt.xlabel('Posición x')
plt.ylabel('Potencial Asociado')
plt.legend()
plt.savefig('problema6.pdf')
plt.show()
