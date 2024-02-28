# Write a program that calculates the division of two numbers entered by the user. Use a try-except block to handle the ZeroDivisionError exception and display an appropriate error message if the user tries to divide by zero.


while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("The result is:", result)
    break  
  except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please enter a non-zero value for the second number.")

print("Calculation complete.")
