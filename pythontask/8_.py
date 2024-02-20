# Write a Python program to reverse a list.
def reverse_list(lst):
    new_lst = lst[::-1]
    return new_lst

original_list = [1, 2, 3, 4, 5, 6]

reversed_list = reverse_list(original_list)

print("Reversed list:", reversed_list)