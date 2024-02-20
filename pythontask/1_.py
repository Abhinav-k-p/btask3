def perform_operations(a, b):
    print("Addition: ", a + b)
    print("Subtraction: ", a - b)
    print("Multiplication: ", a * b)
    print("Exponentiation: ", a ** b)
   
    if b != 0:
        print("Division: ", a / b)
        print("floor division: ", a // b)
        print("modulus" , a % b)
    else:
        print("b should be greater than 0")
        
    
operand1 = float(input("Enter the first operand: "))
operand2 = float(input("Enter the second operand: "))

perform_operations(operand1, operand2)
