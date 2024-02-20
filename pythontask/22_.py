# Write a Python program to check if a given number is a perfect number

def is_perfect_number(number):
    sum_of_divisors = 0

    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == number:
        return True
    else:
        return False

user_input = int(input("Enter a positive integer: "))
if is_perfect_number(user_input):
    print(f"{user_input} is a perfect number.")
else:
    print(f"{user_input} is not a perfect number.")
