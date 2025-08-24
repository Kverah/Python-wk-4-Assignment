#File Read & Write Challenge & Error Handling
def read_and_modify_file():
    #Ask the user for the input file name
    input_file=input("Enter the name of the file to read:")
    
    try:
        #Try to open and read the file
        with open(input_file,'r') as file:
            content= file.read()

            #Modify the content(example:convert to uppercase)
            modified_content=content.upper()

            #Create a new file to save the modified content
            output_file="modified_"+ input_file
            with open(output_file,'w') as file:
                file.write(modified_content)

                print(f"File has been successfully modified and saved as '{output_file}'".)

            except FileNotFoundError:
print(f"Error:The file '{input_file}'does not exist.")
except PermissionError:
print(f"Error:You do not have permission to read '{input_file}'".)
except Exception as e:
print(f"An unexpected error occurred:{e}")