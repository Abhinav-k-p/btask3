# Write a Python program that simulates a banking system. Implement a class called BankAccount with methods to initialize an account with a starting balance, withdraw funds, and handle a custom exception called NegativeBalanceError when the account balance goes below zero.


class NegativeBalanceError(Exception):
    pass
 
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
 
    def withdraw(self, amount):
        if amount > self.balance:
            raise NegativeBalanceError("Insufficient funds: Cannot withdraw more than the available balance.")
        self.balance -= amount
        return amount
 
try:
    initial_balance = 5000
    print(f"initial_balance: {initial_balance}")
    account = BankAccount(initial_balance)
    while True:
        
        ch=input('Type 1 if you want to withdraw or Type 2 if you want to exit: ')
        if ch=='1':
            print("\nCurrent balance:", account.balance)
            withdrawal_amount = float(input("Enter withdrawal amount: "))
            withdrawn = account.withdraw(withdrawal_amount)
            print("Withdrawn amount:", withdrawn)
            print("\nCurrent balance:", account.balance)
        elif ch=='2':
            print("\nCurrent balance:", account.balance)
            print('exit')
            break
except ValueError:
    print("Invalid input! Please enter a valid number.")
except NegativeBalanceError as e:
    print("Error:", e)