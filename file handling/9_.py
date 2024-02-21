# Write a Python program that takes a text file as input and returns the number of words of a given text file.
# Note: Some words can be separated by a comma with no space.

filename = "sample.txt"

number_of_words = 0

with open(filename, 'r') as file:
    data = file.read()
    lines = data.split()
    number_of_words += len(lines)

print(f"Total number of words in '{filename}': {number_of_words}")
