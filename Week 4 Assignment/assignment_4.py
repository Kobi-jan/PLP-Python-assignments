# File Read and Write Challenge
def read_and_write_file(input_file, output_file):
    try:
        # Open the input file 
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Modify the content 
        modified_content = content.upper()

        # Open the output file and add the modified content
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        print(f"File has been successfully written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    finally :
        print("Done")


# Error Handling Lab
def safe_file_read():
    filename = input("Please enter the filename to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally :
        print("Done")


