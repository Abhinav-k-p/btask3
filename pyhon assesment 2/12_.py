# Write a function that takes a sentence as input and returns a new sentence with the words reversed, while keeping the order of the words in the sentence

def reverse_words(sentence):
    # Split the sentence into individual words
    words = sentence.split()  
    # Reverse each word
    reversed_words = [word[::-1] for word in words]  
    # Join the reversed words back into a sentence
    new_sentence = ' '.join(reversed_words)  
    return new_sentence


original_sentence = "Python is awesome"
reversed_sentence = reverse_words(original_sentence)
print("Reversed sentence:", reversed_sentence)
