def issquare(n):
    root = (int)(n**0.5)
    if(root*root == n):
        return True
    else:
        return False

T = int(input("Enter number of testcases: "))
lst = []
for i in range(T):
    n1 = int(input())
    n2 = int(input())
    count = 0
    for j in range(n1, n2+1):
        if(issquare(j)):
            count += 1
            
    lst.append(count)
for i in lst:
    print(i)