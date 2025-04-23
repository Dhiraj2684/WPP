L = int(input())
R = int(input())
MAX = 0
for i in range(L, R+1):
    for j in range(L,R+1):
        if i^j > MAX:
            MAX = i^j
print(MAX)