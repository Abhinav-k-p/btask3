start = lambda stri,char : stri.startswith(char)

string=input("enter the string:")

startwith=input("enter the char start with:")

result = start(string,startwith)

if result:
    print(f"the string start with character {startwith}")
else:
    print(f"dos not start with {startwith}.")