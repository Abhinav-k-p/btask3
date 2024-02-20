# Write a Python program to calculate the sum of all elements in a list recursively

def sum_list(lst):
    if not lst:  
        return 0
    
    first_element = lst[0]  
    rest_of_elements = lst[1:] 
    return first_element + sum_list(rest_of_elements)  

my_list = [3, 5, -7, 9, 8]
result = sum_list(my_list)
print("Sum:", result)