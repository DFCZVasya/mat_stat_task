data = [0.096, 0.052, 0.312, 0.705, 0.850, 0.199, 0.042, 0.798, 0.832, 0.305,
0.526, 0.910, 0.443, 0.531, 0.120, 0.325, 0.334, 0.072, 0.275, 0.420,
0.775, 0.949, 0.185, 0.358, 0.303, 0.175, 0.298, 0.085, 0.874, 0.460]
import numpy as np
import matplotlib.pyplot as plt
import math

def Indecator(num, t):
    return num <= t

def EmpericFunc(t):
    sum = 0
    for num in data:
        sum += Indecator(num, t) / len(data)

    return sum

y = lambda x: EmpericFunc(x)
fig = plt.subplots()

x = np.linspace(-0.1, 1.1,10000)
#%matplotlib widget
plt.plot(x, y(x))
plt.show()

plt.hist(data, range = (0, 1), color = 'blue', edgecolor = 'black', bins = int(math.log2(30) + 1), density = 1)
plt.show()
z = lambda x: x

plt.plot(x, y(x))
plt.plot(x, z(x))
plt.show()