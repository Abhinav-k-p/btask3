# Write a Python program to assess if a file is closed or not

filename = "sample.txt"

file = open(filename, 'r')

if not file.closed:
    print(f"The file '{filename}' is open.")

file.close()

if file.closed:
    print(f"The file '{filename}' is now closed.")
