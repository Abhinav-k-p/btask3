# Write a Python program to write a list to a file

my_list = ['abh', 'hell', 'point', 'fellow']
file_path = 'sample.txt'

with open(file_path, 'w') as file:
    for item in my_list:
        file.write(f"{item}\n")

print(f"The list has been written to {file_path}.")