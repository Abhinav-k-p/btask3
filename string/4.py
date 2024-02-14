#1.capitalize
text = "abhinav"
x = text.capitalize()
print (x)

#2.find
text = "python is a simple language"
x = text.find("a")
print(x)

#3strip
text = "apple"
x = text.strip()
print("of all fruits", x, "is my favorite")

#4.format
test1 = "My name is {fname}, I'm {age}".format(fname = "abhi", age = 26)
test2 = "My name is {0}, I'm {1}".format("abhi",26)
test3 = "My name is {}, I'm {}".format("abhi",26)
print(test1)
print(test2)
print(test3)

#5.isalnum
text = "exmple123"
x = text.isalnum()
print(x)

#6.isalpha
text = "example"
x = text.isalpha()
print(x)

#7.lower
text = "EXAMPLE"
x = text.lower()
print(x)

#8.upper
text = "example"
x = text.upper()
print(x)

#9.replace
text = "sonu is a nice person"
x = text.replace('sonu','abhi')
print(x)

#10.split
text = "today is a fresh day"
x = text.split()
print(x)

#11.count
text = "your company is good.company has lot of employe"
x = text.count('company')
print(x)

#12.index
text = "where is your home"
x = text.index("is")
print(x)

# 13.isdigit
text = "80000"
x = text.isdigit()
print(x)

#14. islower
text = "beyondlove"
x = text.islower()
print(x)

#15. isupper
text = "DESTINY"
x = text.isupper()
print(x)