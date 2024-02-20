# Write a Python program to check if a string contains only digits.

def contains_only_digits(input_string):
    return input_string.isdigit()

user_input = input("Enter a string: ")

if contains_only_digits(user_input):
    print(f"'{user_input}' contains only digits.")
else:
    print(f"'{user_input}' does not contain only digits.")

