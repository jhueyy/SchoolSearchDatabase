def clean_command_log(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if "Enter command:" not in line:
                    outfile.write(line)
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# use command grep -v "Enter command:" input_file_name.txt > output_file_name.txt

#clean_command_log('tests.out', 'cleaned_log.txt')

