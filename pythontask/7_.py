# Write a Python program to implement a binary search on a sorted list.

def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]

        if mid_value == target:
            return f"Target {target} found at index {mid}"
        elif mid_value < target:
            low = mid + 1 
        else:
            high = mid - 1 

    return f"Target {target} not found in the list"

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6

result = binary_search(sorted_list, target)
print(result)
