# a)
# 0
# 0 0
# 0 0 0
# 0 0 0 0

rows = 4

for i in range(rows):
    for j in range(i + 1):
        print("0", end=" ")
    print()  
    
# b)
#        *
#      * * *
#    * * * * *
#  * * * * * * *


rows = 4


for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
  
    print()
# c)  
# 0
# 1 1
# 2 2 2
# 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5 5

rows = 6

for i in range(rows):
    for j in range(i + 1):
        print(i, end=" ")
    print()
    
# d)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows = 5


for i in range(rows):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()
    
# e)
# * * * * * *
# * * * * *
# * * * *
# * * * 
# * *
# *


rows = 6

for i in range(rows):
    for j in range(rows - i):
        print("*", end=" ")
    print() 
    
# f)
# @ @ @ @ @ @ @
# @ @ @ @ @ @ @
# @ @ @ @ @ @ @
# @ @ @ @ @ @ @

rows = 4
cols = 7

for i in range(rows):
    for j in range(cols):
        print("@", end=" ")
    print() 