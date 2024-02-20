# Write a Python program to count the number of occurrences of each element in a tuple

my_tuple = (1, 2, 3, 2, 4, 2, 5, 3, 6, 3, 7, 1, 8, 1)

counts = {}
for element in my_tuple: 
    if element not in counts:
        counts[element] = 1
    
    else:
        counts[element] += 1

for element, count in counts.items():
    print(f"{element}: {count}")