# Read and Print the Contents of a Text File

with open('testing.txt', 'w') as f:
    f.write('Create a new text file!')
    
with open('testing.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
    






    







