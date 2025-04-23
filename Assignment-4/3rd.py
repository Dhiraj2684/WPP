import string
text = input("Enter your text: ")
text = text.lower()
counter = True
for i in string.ascii_lowercase:
    if i not in text:
        counter = False
        break
if(counter):
    print("Panagram")
else:
    print("Not Panagram")