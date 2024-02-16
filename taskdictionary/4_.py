# Write a Python program to sum all the items in a dictionary

n = int(input("Enter the number of key-value pairs: "))
d = {}

for i in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    d[key] = value

result = sum(d.values())

print("Sum of all items in the dictionary:", result)
