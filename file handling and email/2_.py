# Create a program that opens a file and reads its contents. Use a try-except block to handle the FileNotFoundError exception and display a custom error message if the file does not exist.
  
try:
 with open("hello212.txt", "r") as file:  # Replace with the actual file path
   contents = file.read()
   print(contents)
except FileNotFoundError:
 print("Error: File 'non-existent-file.txt' not found.")