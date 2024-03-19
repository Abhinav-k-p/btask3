# Search for a String in a Text File

file_path = 'testing.txt'
search_string = 'beinex'

found = False  # Flag to track if the search string is found in any line

with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        if search_string in line:
            print(f"Found '{search_string}' in line {line_number}: {line.strip()}")
            found = True
            # No need to continue searching if the string is found once
            break

if not found:
    print(f"String '{search_string}' not found in the file.")
