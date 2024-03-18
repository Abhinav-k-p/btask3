# Implement a program that reads a text file and counts the occurrences of each word, ignoring case sensitivity.

import re

def count_word_occurrences(file_name):
    word_count = {}
    with open(file_name, 'r') as file:
        for line in file:
            # Remove non-alphabetic characters and split the line into words
            words = re.findall(r'\b[a-zA-Z]+\b', line.lower())
            for word in words:
                # Update word count
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    file_name = "testing.txt"
    try:
        word_count = count_word_occurrences(file_name)
        print("Word counts:")
        for word, count in word_count.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
