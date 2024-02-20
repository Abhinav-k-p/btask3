# Write a Python program to count the occurrences of an element in a list.

def count_occurrences(lst, x):
    return lst.count(x)

my_list = [8, 6, 8, 10, 8, 20, 10, 8, 8]
element_to_count = 8
print(f"The element {element_to_count} occurs {count_occurrences(my_list, element_to_count)} times")
