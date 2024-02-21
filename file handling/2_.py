# Write a Python program to read first n lines of a file

a = 'sample.txt'
n=1
file = open('sample.txt', 'r')
test = file.readlines()
for line in test[:n]:
    print(line)
file.close