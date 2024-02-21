# Write a Python program to read a file line by line store it into a variable

test = open('sample.txt','r')

check =test.readlines()
for list in check:
    print(list.strip())