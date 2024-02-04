from file_processing import *
'''
This file contains functions the main() function that handles running the user's input'''

# exiting program
def exit_function():
    print("Exiting program...")
    exit(0)

def main():
    valid = False
    # infinite loop
    while True:
        stream_service = None
        # asks the user if they want to update a file.
        if (not valid):
            text = 'Would you like to update a file? Y/N\n'
            valid = True
        else:
            text = 'Would you like to enter another set of files? Y/N\n'

        user_input = str.lower(input(text))

        if not (user_input == 'y' or  user_input == 'n'):
            # raise an error if the input is invalid(not y or n)
            raise Exception(f'{user_input} is not invalid')
        # If the user chooses 'n', then the program exits.
        if user_input == 'n':
            exit_function()
        # If the user chooses 'yes', then they prompts for a filename
        if user_input=='y':
            while True:
                file_name = str(input("Please enter the streaming service creation file (or 'done' to exit):\n"))
                # enter done to exit the program
                if file_name== 'done':
                    exit_function()
                # calls the build_new_service() function from file_processing.py.
                else:
                    stream_service = build_new_service(file_name)
                # warn if the input is invalid that is  excluding existing files
                if (stream_service == None):
                    print("Unfortunately, that file could not be found")
                else:
                    break

            while True:
                # prompts the user for the name of the appropriate update file.
                update_file = input("Please enter the update file you would like to read (or 'done' to exit):\n")
                # type done to exit the program
                if update_file=='done':
                    exit_function()
                # calls the build_new_service function from file_processing.py.
                else:
                    update_stream_service = update_service(update_file, stream_service)
                if (update_stream_service == None):
                    print("Unfortunately, that file could not be found")
                # sort updated file
                else:
                    update_stream_service.sort()
                    break
            # prompts the user for a new filename
            new_file_name = input("Please enter the the name of the new file to be written:\n")
            # type done to exit the program
            if new_file_name == 'done':
                exit_function()
            # calls the write_update() function from file_processing.py
            else:
                write_update(new_file_name, update_stream_service)
                print("Writing updates to", new_file_name,"...")

if __name__ == '__main__':
    main()