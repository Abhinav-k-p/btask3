# Write a Python program to find the sum of all even numbers in a list

def sum_of_evens(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total

my_list = [10,12,13,21,22]

print("Sum of even numbers:", sum_of_evens(my_list))