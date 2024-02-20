# Write a Python program to remove all whitespace characters from a string

def remove_whitespace_replace(input_string):
    return input_string.replace(" ", "")


my_string = "Hello World! This is a test."
result = remove_whitespace_replace(my_string)
print("String after removing whitespace:", result)
