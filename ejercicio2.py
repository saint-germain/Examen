# Ejercicio 2 (20 puntos)
# Resuelva la ecuación de advección lineal d_t u + c d_x u = 0. 
# La condición inicial es una función gaussiana centrada en 0.0 y de sigma 0.1.
# La ecuación debe ser resuelta hasta un tiempo final T=0.5 y una velocidad c=-1.0.
# El programa debe hacer una gráfica (adveccion.png) con la condición incial y el resultado final.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
nx=1001
xmin=-0.5
xmax=0.5
xdel=(xmax-xmin)/nx
x=np.linspace(-0.5,0.5,nx)
u0=np.exp(-x**2/0.1**2)
c=-1
nt=10001
tmin=0
tmax=0.5
t=np.linspace(0,0.5,nt)
tdel=(tmax-tmin)/nt
u=u0
for ti in t:
    dxu=np.gradient(u)/xdel
    u=u-tdel*c*dxu
plt.plot(x,u,label='After')
plt.plot(x,u0,label='Before')
plt.legend()
plt.xlabel('x')
plt.ylabel('u')
plt.savefig('adveccion.png')