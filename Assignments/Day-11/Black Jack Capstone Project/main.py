from art import logo
import os

# Clears the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a card from the deck of cards. ACE is 11"""
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    # Blackjack condition in the base cards returns '0'
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Ace condition check if sum greater then 21 and ace change ace to '1'
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)


def compare(user_score,computer_score):
    """Compares the user score and computer score while also checking the condition of blackjack and returns string"""
    if computer_score == 0:
        return "Computer hit the BlackJack You LOSE!!"
    elif user_score == 0:
        return "You hit the BlackJack You WIN!!"
    elif user_score > 21:
        return "You went over 21! You LOSE !!"
    elif computer_score > 21:
        return "Computer went over 21! You WIN !!"
    elif user_score>computer_score:
        return "You Win"
    else:
        return "You Lose"

# Main Game Function
def play_game():
    print(logo)
    # Card in user and computer's deck
    user_cards = []
    computer_cards = []
    # Checks the blackjack condition occured or not
    is_game_over=False

    # For 2 Base Cards in User and Computer Cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards} and user score is {user_score}")
        print(f" Computer first card is {computer_cards[0]}")


        # Conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over=True
        else:
            user_should_deal= input("Type 'y' to get another card and 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    # Check if computer has value less then 17
    while computer_score!=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"\n\nYou final hand is {user_cards} and score is {user_score}")
    print(f" Computer's final hand is {computer_cards} and score is {computer_score}")
    print(compare(user_score,computer_score))

# new game condition
while input("For new game : 'y' To quit 'n': ") == "y":
    clear()
    play_game()

    