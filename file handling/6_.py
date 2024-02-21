# Write a Python program to read a random line from a file

import random

with open('sample.txt', 'r') as file:
    lines = file.read().splitlines()
    random_line = random.choice(lines)
    print(random_line)