# Write a Python program to find the second largest number in a list.

def second_largest(numbers):
    largest = None
    second_largest = None
    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest

my_numbers = [10, 5, 8, 20, 15]
result = second_largest(my_numbers)
print(f"The second largest number is: {result}")
