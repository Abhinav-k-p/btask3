# Write a Python program to copy the contents of a file to another file

with open('sample.txt', 'r') as firstfile, open('testing.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)