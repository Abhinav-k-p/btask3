# Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])


def flat(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flat(item))
        else:
            result.append(item)
    return result

nested_list = [10, [20, 30], [42, [51, 68]]]
flattened_list = flat(nested_list)
print("Flattened list:", flattened_list)
