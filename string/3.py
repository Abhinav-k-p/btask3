input_user = input("Enter a string: ")

character = input("Enter the character to keep: ")

result = ''.join(char for char in input_user if char == character)

print(f"Expected Result: '{result}'")
