# Python program to delay printing of line from a file using sleep function


import time

# Open the file in 'r' mode for reading
file_path = "notes.txt"
with open(file_path, "r") as file:
    while True:
        char = file.read(1)
        if char == "":
            break
        print(char, end="")
        time.sleep(0.3)


