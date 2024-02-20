# Write a Python program to remove all occurrences of a given element from a list

def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

my_list = [1, 3, 4, 6, 5, 1]
item_to_remove = int(input("enter a number: "))
result = remove_items(my_list, item_to_remove)
print("The list after removing all occurrences of", item_to_remove, "is:", result)

