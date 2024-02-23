# Create a class named Cypher. The purpose of that class is to receive an input string of characters and convert it to 
# another cypher string. Use a constructor to receive the input. You can also read the input from user. But don’t use 
# input() inside the constructor. 
# The class must have a class method to do the string conversion. And an instance method to invoke the classmethod 
# from within it.
# • Use the below conversion logic:
# • Iterate over each character in the string, and if the character is a digit increment it by one (0->1, 1-
# >2, ... 9 should be replaced with 0)
# • if the character is an alphabet then shift the character by 2 positions (use chr() and ord() built-ins for 
# this) (a->c, b->d, ... y->a, z->b) If the character is in upper case convert it to lower and vice versa
# • The returned string must be of same length as the input. 
# No need to implement the reversing algorithm but will be a plus if available.
# 1) create an object for the Cypher class with the string.
# 2) call the instance method, which should internally call the classmethod you prepared for the conversion, pass the 
# string data to classmethod and do the conversion.
# No need to consider special characters for now.
# Expected output for the string "ABcD1293Z" is "cdEf2304b




class Cypher:
    def __init__(self, input_string):
        self.input_string = input_string

    @classmethod
    def convert_string(cls, string):
        
        """Converting string"""
        
        cypher_string = ""
        for char in string:
            if char.isdigit():
                new_char = str((int(char) + 1) % 10) 
            elif char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                new_ord = (ord(char) - base + 2) % 26 + base
                new_char = chr(new_ord)
                new_char = new_char.swapcase()  
            else:
                new_char = char 
            cypher_string += new_char
        return cypher_string

    def create_cypher(self):
        
        """Calls the class method to perform the conversion."""
        
        return self.convert_string(self.input_string)

input_string = "ABcD1293Z"
cypher_obj = Cypher(input_string)
cypher_text = cypher_obj.create_cypher()
print(cypher_text)
