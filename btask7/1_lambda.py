add= lambda x: x + 15
mul= lambda x,y : x * y

number_add=int(input("enter the number"))
result= add(number_add)
print(f"the added number is {result}")

num_x=int(input("enter mul number:"))
num_y=int(input("enter mul number:"))

result_m=mul(num_x,num_y)

print(f"the mul number is {result_m}")

