import random
rand_choice = []
for i in range(100):
    n = random.randint(0,1)
    rand_choice.append(n)
print(rand_choice)

number_list = []
count = 0
for i in range(0,100):
    if (rand_choice[i] == 0):
        count += 1
    else:
        if count>0:
            number_list.append(count)
            count=0
if count>0:
    number_list.append(count)

print("Longest run of zeroes: ",max(number_list))
    