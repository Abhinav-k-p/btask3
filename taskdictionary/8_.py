#Create a function that takes a string and returns a dictionary where keys are letters, and values are the number of times each letter appears in the string 

def count_letters(input_string):
    letter_count = {}

    for char in input_string:
        if char.isalpha():  
            char = char.lower()  
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count

input_str =input("enter the string :")

result_dict = count_letters(input_str)

print("Letter count in the string:", result_dict)
