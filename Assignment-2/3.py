T = int(input("Enter number of testcases: "))
lst = []
for i in range(T):
    num = int(input())
    lst.append(num)
lst2 = []
for i in lst:
    count,num = 0,i
    while num > 0:
        rem = num % 10
        num //= 10
        if rem != 0:
            if i % rem == 0:
                count += 1
        else:
            continue
    lst2.append(count)
for i in lst2:
    print(i)