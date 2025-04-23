import numpy as np
import matplotlib.pyplot as plt
import random

func_str = input("Enter a polynomial function in terms of x (e.g., x**3 - x - 2): ")

f = lambda x: eval(func_str)

a, b = random.uniform(-10, 10), random.uniform(-10, 10)
while f(a) * f(b) > 0:
    a, b = random.uniform(-10, 10), random.uniform(-10, 10)

tolerance = 1e-5
midpoints = []

while abs(b - a) > tolerance:
    midpoint = (a + b) / 2
    midpoints.append(midpoint)
    
    if f(midpoint) == 0:
        break
    elif f(midpoint) * f(a) < 0:
        b = midpoint
    else:
        a = midpoint

midpoints = np.array(midpoints)

plt.plot(range(len(midpoints)), midpoints, marker='o', linestyle='-')
plt.xlabel("Iteration")
plt.ylabel("Midpoint")
plt.show()