# Write a Python program to append text to a file and display the text

filename = "sample.txt"
text_to_append = "hello beinex"

with open(filename, 'a') as file:
   
    file.write(text_to_append)

with open(filename, 'r') as file:
    print("Updated content of the file:")
    print(file.read())
