# Write a Python program to get dictionary keys as a list

n = int(input("Enter the number of key-value pairs: "))
d = {}
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d[key] = value

keys_list = list(d.keys())
print("The keys of the dictionary as a list are:", keys_list)