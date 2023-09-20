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


# plt.plot(time_test, T_test)
# plt.show()




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

def move_random(i):
    if i > 0:
        y = pmean
    else:
        y = qmean
    return y

mean_walk = np.zeros(days)
samples = 100
for j in range(samples):
    r_walk = np.zeros(days)
    r_walk[0] = T_test[0]
    for i in np.arange(1,days):
        u = np.random.uniform(0,1)
        if u < p_prob:
            r = 1  # P[X_k = 1] = p
        else:
            r = -1  # P[X_k= -1] = q
        r_walk[i] = move_random(r)
    walk = r_walk.cumsum()
    mean_walk = mean_walk + walk

mean_walk = samples**(-1) * mean_walk
plt.plot(time_test,T_test)
plt.plot(time_test,mean_walk)
plt.show()