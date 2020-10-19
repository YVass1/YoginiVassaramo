
import os
#functions

def num_selection(message):
    """Prints message parameter and prompts user input
converts user input into an integer."""
    return int(input(f"{message}\n"))

def hold():
    "Prompts user input. Accepts any input."
    input("Enter any key to return to main menu: ")
def try_again():
    "Prompts user input. Accepts any input."
    input("Enter any key to try again: ")
def confirm():
    """ Prompts user confirmation. Only accepts valid int as input."""
    end_loop = False
    while not end_loop:
        confirmation = input("""Would you like to continue with your choice?
[1] No    [2] Yes
Enter a number please: """)
        if not confirmation or confirmation.isspace():
            print("You have not entered anything!")
            try_again()
        elif confirmation.isnumeric() == True:
            if 0 < int(confirmation) < 3:
                if int(confirmation) == 1:
                    confirmation = False
                    return confirmation
                else:
                    confirmation = True
                    return confirmation
                end_loop = True
            else:
                print("You have not entered a valid number. Please enter a number between 1 and 2.")
        else:
            print("Please enter a number only.")
            try_again()

