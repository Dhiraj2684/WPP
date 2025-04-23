T = int(input("Enter the number of testcases: "))
lst = []
for _ in range(T):
    text = input()
    lst.append(text)
for i in lst:
    i = list(i)
    pivot = -1
    swap = pivot
    for j in range(len(i)-2,-1,-1):
        if(i[j] < i[j+1]):
            pivot = j
            break
    if(pivot == -1):
       print("No Answer")
       continue
    for j in range(len(i)-1,pivot,-1):
        if(i[j] > i[pivot]):
            swap = j
            break
    i[pivot],i[swap] = i[swap],i[pivot]
    i[pivot + 1:] = sorted(i[pivot + 1:])
    res = ''.join(i)
    print(res)