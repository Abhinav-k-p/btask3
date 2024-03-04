# Write a function that takes a list of numbers as input and returns the second-largest number

def second_largest(numbers):
    if len(numbers) < 2:
        return "List should have at least two numbers"

    # Sorting the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    # Returning the second element (index 1) in the sorted list
    return sorted_numbers[1]

numbers_list = [10, 5, 8, 20, 15]
result = second_largest(numbers_list)

print(f"The second-largest number is: {result}")

