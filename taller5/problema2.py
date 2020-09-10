# @Author: Diego Sarceno
# Date: 9.09.2020

import numpy as np
import matplotlib.pyplot as plt

def A_Sqrd(omega):
    # Constantes
    w0 = 4
    beta = 0.1
    f0 = 2.2
    return f0**2 / ((w0**2 - omega**2)**2 +4*(beta**2)*(omega**2))

# ARREGLOS
w = np.linspace(0,10,1000)
A = np.zeros(len(w))

for i in range(len(w)):
    A[i] = A_Sqrd(w[i])

# SE GRAFICAN
plt.plot(w,A,'-k',label='$A^2$')
plt.legend()
plt.xlabel('$\omega$')
plt.ylabel('$A^2$')
plt.title('Amplitud')
plt.savefig('problema2.pdf')
plt.show()
