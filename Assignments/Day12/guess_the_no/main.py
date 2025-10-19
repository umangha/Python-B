# Guess The Number Game
from art import logo
import os
import random

# Clears the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
       

def game():
    # Default value
    attempts = 0
    answer = 0

    # Game Start Pack
    clear()
    print(logo)
    print("Thinking I am between 1 to 100. May the force be with you!")
    # Prompt to ask the difficulty from user
    difficulty_setting = input("Choose the Difficulty. 'easy' or 'hard' : ")

    # setting the no of attempts for the user
    if difficulty_setting == "easy":
        attempts=10
    else:
        attempts=5

    # Computer's Guess number
    answer= random.randint(1,100)
    # print(answer)

    # Printing the no of attempts the user has
    print(f"You have {attempts} reamaining to guess the number.")

    # Repeat the game of guessing until the user has attempts above 0
    while attempts > 0:         
        # Prompt to ask the user to guess a number DEFAULT=0
        guess = int(input("Guess a no: ").strip() or "0")

        # Condition check
        if guess == answer:
            print(f"You WIN. Answer is {guess}")
            break
        elif guess > answer:
            print(f"Too HIGH")
            attempts-=1
        elif guess < answer:
            print(f"Too LOW ")
            attempts-=1
        
        # printing the remaining attempts
        if attempts == 0:
            print(f"\nGame Over!! You Lose. Answer is {answer}")
        else:
            print("Guess again")
            print(f"Remaining attempts {attempts}\n")


# Initial calling
game()  
        
# game status
continue_game=input("\nFor new game 'y' and to exit 'e' ")
if continue_game=='y':
    game()    
