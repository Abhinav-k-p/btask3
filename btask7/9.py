def max1(list):
    max1 = max(list, key=lambda i: (isinstance(i, int), i))
    return max1

list = ['Python', 3, 2, 4, 5, 'version']

print("Original list:")
print(list)

print("Maximum values in the said list using lambda:")
print(max1(list)) 