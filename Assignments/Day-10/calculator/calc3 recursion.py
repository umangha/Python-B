# Calculator Updating with Recursion concept after ending the current iteration

import os

# For Clearing the screen
# Clears the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Example usage
clear()
print("The screen is cleared!")

# Add function
def add(number1,number2):
    """Inputs two numbers and returns their sum """
    return number1+number2

# Subtract Function
def subs(number1,number2):
    """Inputs two numbers and returns their substraction"""
    return number1-number2

# Multiply Functin
def mul(number1,number2):
    """Inputs two numbers and returns their multiplication"""
    return number1*number2

# Division Function
def div(number1,number2):
    """Inputs two numbers and returns their divison"""
    return number1/number2



# Creating a dicionary to store the values of operation
# "KEY" is the operation(+,-,*,/) and "VALUES" is the function of the respective operation
# Helps in using the key to get the particular function we want
operation={
    "+":add,
    "-":subs,
    "*":mul,
    "/":div,
}

# Using recursion
def calculator():
    # Clear the screen Calls above function
    clear()

    # Asking the user for the first input
    first_no=int(input("Enter the first number: "))

    # print the symbols using the dicitonary
    for symbol in operation:
        print(symbol)

    # Shows program status should it continue it or not?
    program_status=True
    while program_status:

        # Asking the operation user want to perform
        operation_symbol=input("Pick an operation from the above line:")

        # For better user experience asking the second no after printing the symbols
        second_no=int(input("Enter the next number: "))

        # To execute the function we need the function name
        calculation_func=operation[operation_symbol]
        final_answer=calculation_func(number1=first_no,number2=second_no)

        # Final code to execute
        print(f"{first_no} {operation_symbol} {second_no} = {final_answer}")

        # For asking if they want another nuumber
        another_number=input("Type'y' to continue, 'n' to start from begginning and 'e' to exit : ")
        
        if another_number=="y":
            # Updating the answer if this is run again to the first number
            final_answer=first_no

        elif another_number=="n":
            program_status=False
            calculator()
        else:
            # print("Enter either 'y' or 'n' !!!")
            program_status=False
            clear()

# User of recursion
calculator()
