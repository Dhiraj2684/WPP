def isFibo(n):
    num1 = 5*n*n+4
    num2 = 5*n*n-4
    if(num1**0.5 == int(num1**0.5) or num2**0.5 == int(num2**0.5)):
        return True
    else:
        return False
T = int(input("Enter number of testcases: "))
lst = []
for i in range(T):
    num = int(input())
    lst.append(num)
for i in lst:
    if(isFibo(i)):
        print("IsFibo")
    else:
        print("IsNotFibo")    