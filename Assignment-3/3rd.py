def height_calculator(n):
    height = 1
    for i in range(1,n+1):
        if i%2 != 0:
            height *= 2
        else:
            height += 1
    return height
T = int(input("Enter the number of testcases: "))
lst = []
for i in range(T):
    num = int(input())
    lst.append(num)
for i in lst:
    height = height_calculator(i)
    print(height)
