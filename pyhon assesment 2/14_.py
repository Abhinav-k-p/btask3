# Create a class named Notes for handling text-based file operations. Class should contain methods "write", "read" and then "append" as instance methods or class methods. (Can contain any other methods if you wish) Use a single file for saving the notes. You can set the file name as a constant somewhere in the program (Or as a class variable). write method should create the if it doesn't exist, Then it should overwrite the older contents with the user input if the user plans to overwrite the file. read method should read the whole file contents and return it. If the file doesn't exist, then it should return "No notes found" append method should take the user input value and it must add the value to the end of the file. It must not overwrite the file. Now create a program to utilize this class. The program should repeatedly ask the user for these 4 choices : 
#     1 - Write Note (Overwrite existing). 
#     2 - Add more Notes (Append). 
#     3 - Read Notes. 
#     4 – Exit


class Notes:
    FILENAME = "notes.txt"  

    @staticmethod
    def write(note):
        """Write the note to the file (overwriting existing content)."""
        with open(Notes.FILENAME, "w") as file:
            file.write(note)
        print("Note written successfully!")

    @staticmethod
    def read():
        """Read the entire file contents and return them."""
        try:
            with open(Notes.FILENAME, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "No notes found."

    @staticmethod
    def append(note):
        """Append the note to the end of the file."""
        with open(Notes.FILENAME, "a") as file:
            file.write("\n" + note)
        print("Note appended successfully!")

def main():
    while True:
        print("\nMenu:")
        print("1. Write Note (Overwrite existing)")
        print("2. Add more Notes (Append)")
        print("3. Read Notes")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            note = input("Enter your note: ")
            Notes.write(note)
        elif choice == "2":
            note = input("Enter the additional note: ")
            Notes.append(note)
        elif choice == "3":
            print(Notes.read())
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

