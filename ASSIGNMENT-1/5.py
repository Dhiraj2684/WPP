n = int(input("Enter the number of students: "))
names = []
print("Maximum allowed characters: 15")
for i in range(n):
    name = input("Enter name of student: ")
    names.append(name)
for i in names:
    print(i[len(i)-1:len(i)-16:-1])