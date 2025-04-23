text = input("Enter your text: ")
lst = []
for i in range(len(text)):
    if i%2 != 0:
        lst.append(text[i].upper())
    else:
        lst.append(text[i])
updated = ''.join(lst)
print(updated)