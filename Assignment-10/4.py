import math
import numpy as np
N = int(input("Enter the number of points: "))
lst =  []
print("Enter points: ")
for i in range(N):
    a = float(input())
    b = float(input())
    lst.append((a,b))
array = np.array(lst)
print("cartesian Coordinates: ")
print(array)
lst2 = []
for i in lst:
    r = (i[0]**2 + i[1]**2)** 0.2
    theta = math.degrees(math.atan2(i[1],i[0]))
    lst2.append((r,theta))
array2 = np.array(lst2)
print("Polar Coordinates: ")
print(array2)