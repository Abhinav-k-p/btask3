# Write a program that opens a file, reads its contents, and writes the contents to a new file. Use a try-except-finally block to ensure that the file is closed even if an exception occurs during the file operations.


def copy_file_content(source_file, destination_file):


  try:
 
    with open(source_file, "r") as source:
        contents = source.read()

    # Open the destination file in write mode
    with open(destination_file, "w") as destination:
      # Write the contents to the destination file
      destination.write(contents)

    print(f"Successfully copied contents from '{source_file}' to '{destination_file}'.")
  except FileNotFoundError as e:
    print(f"Error: File '{e.filename}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")
  finally:
    pass  

source_file = "source.txt"
destination_file = "copy.txt"
copy_file_content(source_file, destination_file)
