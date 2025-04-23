T = int(input("Enter number of testcases: "))
lst = []
res = []
for _ in range(T):
    num = int(input())
    lst.append(num)
for i in lst:
    mid = i//2
    res.append(mid*(i-mid))
for _ in res:
    print(_)
