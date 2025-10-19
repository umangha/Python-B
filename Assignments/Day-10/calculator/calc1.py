# Calculator Start

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

# Main Loop
status=True

# Creating a dicionary to store the values of operation
# "KEY" is the operation(+,-,*,/) and "VALUES" is the function of the respective operation
# Helps in using the key to get the particular function we want
operation={
    "+":add,
    "-":subs,
    "*":mul,
    "/":div,
}


# while status:
#     first_no=int(input("Enter the first number: "))
#     second_no=int(input("Enter the second number: "))
#     operation=input("What Operation you want to perform?\n+\n-\n*\n/\n")
#     if operation=="+":
#         add(number1=first_no,number2=second_no)
#     elif operation=="-":
#         subs(number1=first_no,number2=second_no)
#     elif operation=="*":
#         mul(number1=first_no,number2=second_no)
#     elif operation=="/":
#         mul(number1=first_no,number2=second_no)
#     else:
#         print("ERROR ERROR !! Please enter valid symbol!! Exiting......")
#         status=False
    
# Asking the user for the first input
first_no=int(input("Enter the first number: "))

# print the symbols using the dicitonary
for symbol in operation:
    print(symbol)

# Asking the operation user want to perform
operation_symbol=input("Pick an operation from the above line:")

# For better user experience asking the second no after printing the symbols
second_no=int(input("Enter the second number: "))


# To execute the function we need the function name
calculation_func=operation[operation_symbol]
answer=calculation_func(number1=first_no,number2=second_no)


# Final code to execute
print(f"{first_no} {operation_symbol} {second_no} = {answer}")