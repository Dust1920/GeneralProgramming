import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Aqui intentaremos estimar T con una caminata aleatoria.
"""
# Extraemos los datos para aproximar. 

seattle = pd.read_csv("seattle-weather.csv")

# Datos reales
T = pd.to_numeric(seattle['temp_max'])
time = pd.to_datetime(seattle['date'])

# Datos de prueba 
days = 400
T_test = T[:days]
time_test = time[:days]


plt.plot(time_test, T_test)
plt.show()

# Caso 1: h_1 = h_2 = h

h = 1

r_walk = np.zeros(days)
