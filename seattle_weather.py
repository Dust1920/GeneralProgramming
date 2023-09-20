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
T_test = np.array(T[:days])
time_test = np.array(time[:days])


plt.plot(time_test, T_test)
plt.show()

# Caso 1: h variable.

T_test_r = np.roll(T_test, -1)
T_increments = T_test_r - T_test
T_increments = np.delete(T_increments, -1)
print(T_increments)
p = 0
q = 0
h_plus = []
h_minus = []
for i in T_increments:
    if i>0:
        p += 1
        h_plus.append(i)
    else:
        q += 1
        h_minus.append(i)

p_prob = p / days  # p
q_prob = q / days  # q

hpos = np.array(h_plus)
hneg = np.array(h_minus)

pmean = hpos.mean()  # h_1
qmean = hneg.mean()  # -h_2

print(p_prob, pmean, q_prob, qmean)