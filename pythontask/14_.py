# Write a Python program to check if a given year is a leap year

def is_leap(year):
   
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False

year = 1804
if is_leap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")