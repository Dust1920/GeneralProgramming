"""
Movimiento Browiano.
"""

import numpy as np

N = 5 # Puntos
x = np.linspace(0,1, N)

dt = 1 / (N-1)

print(x)

# [0,1], quiero N incrementos. N Dt = 1

# 0 0.2 0.7 1  Dt_i = t_{i+1}-t_{i}