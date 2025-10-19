from guess_the_no.art import logo
import os
import random

# Global Constant Variable setting the no of attempts
EASY_MODE=10
HARD_MODE=5

# Clears the terminal screen
def clear():
    '''Clears the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

# Function that sets the difficulty according to the user
def difficulty():
    '''Returns either EASY_MODE or HARD_MODE '''
    level=input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level == 'easy':
        return EASY_MODE
    else:
        return HARD_MODE



# # User guess checking function
# def compare_guess(guess,answer,attempts):
#     '''Takes guess , answer and attempts and returns attempt-1'''
#     if guess > answer:
#         if (guess-10) > answer:
#             print("Too High")
#         else:
#             print("Little High. Go Lower")
#         return attempts-1
#     elif guess < answer:
#         if guess < (answer-10):
#             print("Too Low")
#         else:
#             print("Little Low. Go Higher")
#         return attempts-1
#     else:
#         print(f"\nYou win!! The answer is {answer}")

# User guess checking function
def compare_guess(guess, answer, attempts):
    '''Takes guess, answer, and attempts and returns attempts - 1.'''
    difference = abs(guess - answer)  # Calculate the absolute difference
    
    if guess > answer:
        if difference > 15:
            print("Too High. Try a much lower number.")
        elif difference > 10:
            print("You're somewhat high. Go lower.")
        elif difference > 5:
            print("You're getting close, but still a bit high.")
        else:
            print("Super close! Just a little lower.")
    elif guess < answer:
        if difference > 15:
            print("Too Low. Try a much higher number.")
        elif difference > 10:
            print("You're somewhat low. Go higher.")
        elif difference > 5:
            print("You're getting close, but still a bit low.")
        else:
            print("Super close! Just a little higher.")
    else:
        print(f"\nYou win!! The answer is {answer}")
    
    return attempts - 1





# Global game() funcion
# Game start
def game():
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Default value of attempts
    attempts = 0
    # Calling Function for choosing difficulty
    attempts = difficulty() 

    # Answer
    answer = random.randint(0,100)
    # print(f"Answer is {answer}")

    # Setting default value for 'guess' because guess is asked from user inside the while loop
    guess = 0
    while guess != answer :
        # Shows the no of attempts to user
        print(f"The remaining attempts are : {attempts}\n")

        # User guess
        guess = int(input("Make a guess : ").strip() or "0")

        # Check the user guess against the answer
        attempts = compare_guess(guess,answer,attempts)

        # If attempts is 0 then return from the main function to exit the function and end the game
        if attempts == 0:
            print(f"\nYou have lost the game. Answer is {answer}")
            return
        else:
            print("Guess again")

# Calling the main game() function
game()

# Looping till user wants to play
while input("Want to continue the game? : 'y' or 'n': ") == 'y':
    game()

clear()