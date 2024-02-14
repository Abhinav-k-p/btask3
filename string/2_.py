test = input("Enter the string :")

words = test.split()

even_length_words = [word for word in words if len(word) % 2 == 0]

result = ", ".join(even_length_words)
print(f"Even length words in the string: {result}")
