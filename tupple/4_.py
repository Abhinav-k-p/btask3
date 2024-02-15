my_list = [24, 34, 53, 65, 78, 93, 23, 42]

new_list = []

for i in my_list:
    if i % 2 != 0:
        new_list.append(i)
        
print(new_list)