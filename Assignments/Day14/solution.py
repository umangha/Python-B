import os
import random

from followers_game.art import logo, vs
from followers_game.game_data import data
# from data import data


# Clears the terminal screen
def clear():
    '''Clears the termianl'''
    os.system('cls' if os.name == 'nt' else 'clear')

def account_detail(account):
    '''Returns the name, description and country of the account(dict)'''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    acccount_followers = account["follower_count"]
    # Returning the detail as fstring
    # return f"{account_name}, a {account_desc}, from {account_country}"
    return f"{account_name}, a {account_desc}, from {account_country}, followers count: {acccount_followers} million"

def check_guess(guess, followers_a, followers_b):
    '''Takes user's guess and follower count from account A and B. Returns Boolean for user_guess'''
    # Table made between A and B and user's correct guess to simplify the solution
    if followers_a > followers_b:
        # Basically means if user's guess is 'a' and answer is 'a' then this condition will be True else false
        return guess == "a"
    elif followers_b > followers_a:
        return guess == "b"
    else:
        # Return none in case of tie
        return None


# Main Game Logic
###################################################
def game():
    '''Main Game Function with game logic '''
    # Printing the logo
    print(logo)

    # User's score
    score = 0

    # Game Loop status
    game_continue = True

    # Here data is List containing multiple dictionary
    # Generating random accounts for A
    account_a = random.choice(data)

    # Loop the Game till the User is incorrect
    while game_continue:

        # Generating random accounts for B
        account_b = random.choice(data)

        # Check if both the account have same value
        # Runs till the account b is different from account a
        while account_a == account_b:
            account_b = random.choice(data)

        # Function to display account detail
        print(account_detail(account_a))

        # VS ASCII art
        print(vs)

        print(account_detail(account_b))

        # User's guess between account A and B
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Number of followers for account A and B
        followers_a = account_a["follower_count"]
        followers_b = account_b["follower_count"]

        # Status of user's guess
        is_correct = check_guess(guess,followers_a,followers_b)

        # Clearing the console for next Game loop
        clear()
        print(logo)

        # Codition for user's guess TRUE or FALSE or None(for tie)
        if is_correct is None:
            # Both account A and B have same followers
            print(f"Score are tied. Score is same {score}")
        elif is_correct:
            # User is Correct
            score +=1
            print(f"You're right! Current score: {score}.")
        else:
            # User is incorrect
            # Game END Condition
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
        
        # Putting account B in account A to continue the next round of guessing
        account_a = account_b

# initialize Game
game()