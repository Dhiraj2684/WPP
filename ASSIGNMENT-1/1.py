lst1=[]
lst2=[]
lst3=[]

for i in range(50):
    lst1.append(i)
print("List 1: ",lst1)
print("\n")
for i in range(1,51):
    lst2.append(i*i)
print("List 2: ",lst2)
print("\n")
char = 'a'
for i in range(1,27):
    lst3.append(chr(ord(char)+i-1)*i)
print("List 3: ",lst3)
