# Ejercicio 1 (10 puntos)
# Calcule integral de exp(x) entre 0 y 1 con el método de trapecio y de Simpson.
# Haga una grafica (error.png) del error fraccional entre la solución numérica y 
# analítica como funcion del numero de puntos (desde N=10 hasta N=10^8). 
# Tanto el error como el numero de puntos deben variar en escala logaritmica.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
earr=[]
sarr=np.arange(1,8)
narr=10**sarr
tval=np.exp(1)-np.exp(0)
for n in narr:
    x=np.linspace(0,1,n)
    y=np.exp(x)
    earr+=[(np.trapz(y,x)-tval)/tval]
plt.plot(sarr,np.log10(earr))
plt.xlabel(r'$\log N$')
plt.ylabel(r'$log$ Fractional Error')
plt.savefig('error.png')

