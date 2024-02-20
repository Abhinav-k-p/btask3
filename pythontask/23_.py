# Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.

def find_gcd_rec(a, b):
    if b == 0:
        return a
    else:
        return find_gcd_rec(b, a % b)

num1 = 48
num2 = 60
print(f"The GCD of {num1} and {num2} is:", find_gcd_rec(num1, num2))
