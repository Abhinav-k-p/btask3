# Write a program to check the validity of a password. Primary conditions for password validation:
# - minimum 8 charecters
# - The alphabet must be between [a-z]
# - At least one alphabet should be of Upper Case [A-Z]
# - At least 1 number or digit between [0-9].
# - At least 1 character from [ _ or @ or $ ]


def is_valid_password(password):
    if len(password) < 8:
        return False

    lowercase = any(c.islower() for c in password)
    uppercase = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    special_char = any(c in '_@$' for c in password)

    return lowercase and uppercase and digit and special_char

user_password = input("Enter a password: ")
if is_valid_password(user_password):
    print("Valid Password")
else:
    print("Invalid Password")
