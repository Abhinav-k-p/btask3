tup = (1, 2, 3, 4, 4, 5, 5, 6, 6, 7)
repeated_items = []


for i in tup:
    if tup.count(i) > 1 and i not in repeated_items:
        repeated_items.append(i)
        
        
print(repeated_items)