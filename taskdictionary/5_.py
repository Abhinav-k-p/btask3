# Write a Python program to multiply all the items in a dictionary

my_dict = {'a': 2, 'b': 3, 'c': 4, 'd': 5}

result = 1

for value in my_dict.values():
    result *= value

print("Multiplication of all items in the dictionary:", result)
