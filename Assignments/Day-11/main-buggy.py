from art import logo
import random
import os

# Clears the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1. 
# An Ace will have a value of 11 unless that would give a player or the dealer a score in excess of 21; in which case, it has a value of 1.
## Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Function to draw and return a random card from the deck
def deal_card():
    '''Returns a Random Card from a deck of card where face card has value 10'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Cards for user and computer
user_card=[]
computer_card=[]

##################### NOT NEEDED
# Winning status
lose_status=False
win_status=False

##################### NOT NEEDED
# For appending a card to user list
def user_append():
    """Appends a single Card in User List"""
    card=deal_card()
    user_card.append(card)

##################### NOT NEEDED
# For appending a card to computer list
def computer_append():
    """Appends a single Card in Computer List"""
    card=deal_card()
    computer_card.append(card)

################ NOT NEEDED
# Starting Cards for both User and Computer
def base_cards():
    """Returns with 2 base cards for both user and computer"""
    for i in range(2):
        # 2 Base card for user
        user_append()

        # 2 Base card for computer
        computer_append()


# Caculate the sum of the cards Condition for Blackjack is checked here!!
def calculate_score(list):
    """Return sum of elements of list"""
    return sum(list)

##################### NOT NEEDED

# Check for Blackjack
def blackjack(user_score,computer_score):
    """Checks initial Ace + 10 Condition"""
    if computer_score == 21 or user_score == 21:
        if user_score == 21:
            win(user_score,computer_score)
        else:
            lose(user_score,computer_score)

# Compare User and computer score
def compare(user_score,computer_score):
    """Compares the Score of User and Computer. Win Lose or Draw"""
        # Final Comparision between the User and Computer Score
    if user_score>computer_score:
        win(user_score,computer_score)
    elif user_score<computer_score:
        lose(user_score,computer_score)
    else:
        print(f"Your score is {user_score} and Computer(Dealer) score is {computer_score}")
        print("ITS A DRAW!!")
        
##################### NOT NEEDED
##################### Should have been inside the compare score function
# Function Checks if user is above 21 considering the ace 11 and 1 value
def check_user(user_sum,computer_sum):
    """Check User score > 21 or not"""
    # Checking if User Score is above 21
    if user_sum> 21:
        # Handling the condition of Ace
        if 11 in user_card:
            # Finding the index of "11" in user cards and using it to replace with 1
            index_of_11=user_card.index(11)
            # print(index_of_11)
            user_card[index_of_11]=1
        else:
            # LOSE
            lose(user_score=user_sum,computer_score=computer_sum)
##################### NOT NEEDED
##################### with the flow of the program after the 
def check_computer(user_sum,computer_sum):
    """Check if computer score > 17"""
    # Calculating the computer final score
    while computer_sum < 17:
        computer_append()
        computer_sum = calculate_score(computer_card)
    if computer_sum > 21:
        win(user_sum, computer_sum)


##################### NOT NEEDED
# Losing Statement
def lose(user_score,computer_score):
    """Prints You Lose With User and Computer Score"""
    global lose_status
    lose_status=True
    # print(f"Your score is {user_score} and Computer(Dealer) score is {computer_score}")
    print("You Lose 😭😭😭😭😭")

##################### NOT NEEDED
# Win Statement
def win(user_score,computer_score):
    """Prints You Win With User and Computer Score"""
    global win_status
    win_status=True
    # print(f"Your score is {user_score} and Computer(Dealer) score is {computer_score}")
    print("You Win 🏆🏆🏆🏆🏆🏆")

##################### NOT NEEDED Too much
# Display curernt cards in User
def display_user_card(user_sum):
    """Prints the the user card list and user sum and also the computer first card"""
    if computer_card:
        print(f"User Cards are: {user_card} and their sum is: {user_sum}\nComputer card is: {computer_card[0]}")
    else:
        print(f"User Cards are: {user_card} and their sum is: {user_sum}")

##############################################################################################
##############################################################################################
##############################################################################################
def main():
    clear()
    # Starting Logo
    print(logo)
    # Setting the base cards for both user and computer(dealer)
    base_cards()

    # Calculating the sum of base 2 cards
    user_sum=calculate_score(user_card)
    computer_sum=calculate_score(computer_card)

    # Check if Black Jack Condition has occurred
    blackjack(user_score=user_sum,computer_score=computer_sum)

    display_user_card(user_sum)

    check_user(user_sum,computer_sum)
    # check_computer(user_sum,computer_sum)

    # Overall Game Status
    game_status= True

    while game_status:
        # Status of the game after winnnig or losing
        if lose_status or win_status:
            game_status=False
            
        
        # Drawing another card
        another_card=input("Type 'y' to draw another card and 'n' to get result !! ")
        if another_card=="y":
            new_card=user_append()
            # Update User score card due to increase of card in the User Card List
            user_sum=calculate_score(user_card)
            display_user_card(user_sum)
            check_user(user_sum,computer_sum)

        elif another_card=="n":
            check_computer(user_sum,computer_sum)
            compare(user_sum,computer_sum)
            game_status=False
            another_game=input("Do you want to play a new game? 'y': ")
            if another_game!="y":
               break

# For Main Game to work
main()
