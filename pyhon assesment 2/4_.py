# Merge Multiple Text Files into One

def merge_files(filenames, output_filename):


  with open(output_filename, 'w') as out_file:
    for filename in filenames:
      with open(filename, 'r') as f:
        out_file.write(f.read())

filenames = ["testing.txt", "hello.txt",]
output_filename = "merged_file.txt"
merge_files(filenames, output_filename)

