original_set = set()
set_0 = set()
set_1 = set()
set_2 = set()
set_3 = set()
set_4 = set()
for i in range(1,10001):
    original_set.add(i)

    if(i % 5 == 0):
        set_0.add(i)
    elif(i % 5 == 1):
        set_1.add(i)
    elif(i % 5 == 2):
        set_2.add(i)
    elif(i % 5 == 3):
        set_3.add(i)
    elif(i % 5 == 4):
        set_4.add(i)

union_set = set_0 | set_1 | set_2 | set_3 | set_4
print(f"Class 0: {set_0}\n")
print(f"Class 1: {set_1}\n")
print(f"Class 2: {set_2}\n")
print(f"Class 3: {set_3}\n")
print(f"Class 4: {set_4}\n")

if (original_set-union_set):
    print("It is not Equivalence Class")
else:
    print("It is Equivalence CLass")