import numpy as np
lst = []
N = int(input("Enter the number of terms: "))
for _ in range(N):
    a = int(input())
    lst.append(a)
lst = list(map(str,lst))
arr = np.array(lst)
centered = np.array([x.center(15,"_") for x in lst])
left = np.array([x.ljust(15,"_") for x in lst])
right = np.array([x.rjust(15,"_") for x in lst])
print(centered)
print(left)
print(right)