# Write a Python program to count the number of vowels in a string

def count_vowels_linear_scan(string):
    vowels = "AEIOUaeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = "Geeks for Geeks"
print("Total number of vowels:", count_vowels_linear_scan(input_string))
