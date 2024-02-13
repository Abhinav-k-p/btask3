palindrome= lambda p: p== p[::-1]

my_list=["friends","malayalam","beyond","future"]

pali= list(filter(palindrome, my_list))

print(pali)