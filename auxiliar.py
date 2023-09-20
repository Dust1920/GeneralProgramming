import matplotlib.pyplot as plt
import numpy as np

prng = np.random.RandomState(10)

def heaviside(x):
    if x<0:
        y = 0
    else:
        y = 1
    return y
    
def indicate(x,a,b):
    if a < x < b:
        y = 1
    else:
        y = 0
    return y

def brownian_motion(rt,n_t):
    time = np.linspace(0,rt,n_t)
    delta_t = time[1]-time[0]
    dw = np.sqrt(delta_t) * np.random.standard_normal(n_t - 1)
    dw = dw.cumsum()
    w = np.zeros(n_t)
    w[1:] = dw
    return time,w

def poisson_motion(rt,n_t,lam):
    time = np.linspace(0,rt,n_t)
    dp = np.array([np.random.poisson(lam * i, 1) for i in time[1:]])
    dp = dp.cumsum()
    p = np.zeros(n_t)
    p[1:] = dp
    return time,p

def poisson_finite_motion():
    n_1= 78
    n_2 = 10
    l = 0.2
    x_e = prng.exponential(l, n_2)
    tau = np.zeros(n_2 + 1)
    tau[1:] = x_e
    tau = tau.cumsum()
    time = np.linspace(0, 100, n_1)
    ns = np.zeros(n_1)
    for j in np.arange(1,n_1):
        i = 0
        n = 0
        while tau[i] < time[j]:
            n += 1
            # print(tau[i], n)
            i += 1
            if i == n_2:
                break
    ns[j] = n

def poisson_motion(t,n_t):
    x_e = [0]
    i = 0
    nt = np.zeros(n_t)
    time = np.linspace(0,t,n_t)
    for j in np.arange(1,n_t):
        while x_e[i] < time[j]:
            v = prng.exponential(1)
            x_e.append( x_e[i]+ v)
            # print(i, x_e[i])
            i += 1
        nt[j] = i
    return time, nt

t, p = poisson_motion(20,100)
plt.plot(t,p)
plt.show()