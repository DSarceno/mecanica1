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
'''el primer arreglo define cuantos puntos de tiempo se van a valuar
y el segundo es un arreglo conformado por ceros que luego seran sustituidos
por el valor de la funcion para ese instante de tiempo'''
t = np.linspace(0,50,100)
r = np.zeros(len(t))

# SE VALUA LA FUNCION (tomando cada tiempo, valuandolo y sustituyendolo en el
# segundo arreglo)
for i in range(len(t)):
    r[i] = x(t[i])

# SE PLOTEA
# grafica la funcion en color negro y una linea continua
plt.plot(t,r,'-k',label='$x(t)$')
# muestra la leyenda dada por 'label' en el comando pasado
plt.legend()
# nombres de cada uno de los ejes
plt.xlabel('Tiempo')
plt.ylabel('Posicion')
# titulo del grafico
plt.title('Problema 5')
# nombre y extencion de la grafica (se guarda en la carpeta donde este el prog.)
plt.savefig('problema5.pdf')
# se muestra la grafica
plt.show()
