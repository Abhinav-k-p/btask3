list1=[2,4,6,9,11]

mul_num=2
result = list(map(lambda x: x * mul_num, list1))

print(f"Original list: {list1}")
print(f"Given number: {mul_num}")
print(f"Result: {result}")