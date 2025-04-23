import pandas as pd
user_input = input("Enter strings separated by commas: ")
data = pd.Series(user_input.split(','))

upper_case = data.str.upper()

lower_case = data.str.lower()

string_lengths = data.str.len()

print("Original Series:")
print(data)
print("\nUppercase:")
print(upper_case)
print("\nLowercase:")
print(lower_case)
print("\nString Lengths:")
print(string_lengths)