length = float(input("Enter length in feet: "))
print("1.Inches\n2.Yards\n3.Miles\n4.millimetres\n5.Centimetres\n6.Metres\n7.Kilometres")
choice = int(input("Enter your choice for conversion: "))
result = [12,0.333,0.000189394,304.8,30.48,0.3048,0.0003048]

if choice <= 7 and choice >= 1:
    print(length*result[choice-1])
else:
    print("Enter valid choice!!")