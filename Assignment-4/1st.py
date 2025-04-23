T = int(input("Enter the number of testcases: "))
input_list = []
for i in range(T):
    text = input()
    input_list.append(text)
output_list = []
for i in input_list:
    count = 0
    for j in range(len(i)//2):
        if(ord(i[j]) >= ord(i[len(i)-j-1])):
            count += ord(i[j]) - ord(i[len(i)-j-1])
        elif(ord(i[j]) <= ord(i[len(i)-j-1])):
            count += -ord(i[j]) + ord(i[len(i)-j-1])
    output_list.append(count)
for i in output_list:
    print(i)