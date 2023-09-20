"""
Practicas para Susana
"""

import numpy as np

import scipy as sp


x = np.linspace(0, 10, 100)

y = np.arange(0, 10, 10)


"""
Metodo 1: linspace (Decide el espacio de los puntos)

- Todos los valores estan entre 0 y 10. (Primer y Segundo parametro)
- linspace arroja vectores. (Tamaño 100, Tercer parametro)
- Elementos del vector estan separados por la misma distancia.

"""


"""
Metodo 2: Arange (Decide el numero de puntos)
- arange arroja vectores
- Contiene valores entre 0 y 10, (excepto el 10) (primer, segundo parametro)
- Separados por 0.2 (Tercer parametro)
"""

"""Problema 1
    Dada f, aproxime la integral de 0 a 10
"""

def f(x):
    y = np.exp(x)
    return y

"""
Paso 1: Tomar una particion
"""
n = 100
particion = np.linspace(0,10, n)

"""
Paso 2: Evaluar f en la particion

"""
fx = np.zeros(n)

j = 0
for i in particion:
    fx[j]=f(i)
    j = j + 1

"""
Metodo 3:  zeros
- zeros devuelve vector
- El objeto contiene solo ceros
- el objeto tiene dimension n ("unico" parametro)
"""

"""
Paso final: Sumar fx
"""

integral = 0
for i in fx:
    integral += i

print(integral * (particion[1]-particion[0]))  # x_1-x_0

"""Preguntas
¿El codigo esta mal? No, porque funciona. 
¿Porque salio ese valor? 
"""