# Copy odd lines of one file to another file in Python


def copy_odd_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_number, line in enumerate(infile, 1):
            if line_number % 2 != 0:
                outfile.write(line)

input_file_name = 'input.txt'
output_file_name = 'output1.txt'
copy_odd_lines(input_file_name, output_file_name)

