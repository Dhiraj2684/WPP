n = int(input("Enter number: "))
while n > 9:
    sum = 0
    while n > 0:
        sum += n%10
        n //= 10
    n = sum
print(sum)