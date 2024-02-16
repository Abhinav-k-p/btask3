# Write a Python program to Delete a list of keys from a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

keys_to_delete = ['b', 'd']

for key in keys_to_delete:
    if key in my_dict:
        del my_dict[key]
    else:
        print(f"Key '{key}' not found in the dictionary.")

print("Updated dictionary after deleting keys:", my_dict)
