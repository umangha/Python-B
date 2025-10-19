from guess_the_no.art import logo
import os
import random

# Clears the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Global variables for game settings
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def get_valid_guess():
    """Prompt user for a valid number guess and handle invalid input."""
    while True:
        try:
            guess = int(input("Guess a number: ").strip())
            return guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def check_guess(guess, answer):
    """Check if the user's guess is correct, too high, or too low."""
    if guess == answer:
        print(f"🎉 You WIN! The correct answer is {answer}.\n")
        return True
    elif guess > answer:
        print("Too HIGH. Try again!")
    else:
        print("Too LOW. Try again!")
    return False

def set_difficulty():
    """Set difficulty based on user input."""
    while True:
        difficulty = input("Choose the Difficulty ('easy' or 'hard'): ").lower()
        if difficulty == "easy":
            return EASY_ATTEMPTS
        elif difficulty == "hard":
            return HARD_ATTEMPTS
        else:
            print("Invalid choice! Please enter 'easy' or 'hard'.")

def game():
    """Main function to run the guessing game."""
    clear()
    print(logo)
    print("🎮 Welcome to 'Guess The Number'! I’m thinking of a number between 1 and 100.")

    # Set difficulty and attempts
    attempts = set_difficulty()
    answer = random.randint(1, 100)  # Computer's number
    print(f"\nYou have {attempts} attempts to guess the number.\n")

    # Game loop
    while attempts > 0:
        guess = get_valid_guess()  # Get user's guess
        if check_guess(guess, answer):  # Check if guess is correct
            break
        attempts -= 1  # Reduce attempts after each guess

        if attempts > 0:
            print(f"Remaining attempts: {attempts}\n")
        else:
            print(f"😢 Game Over! You've used all attempts. The answer was {answer}.\n")

# Run the game in a loop
while True:
    game()
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("👋 Thanks for playing! Goodbye!")
        break
