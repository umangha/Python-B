from art import logo, vs
from game_data import data
import random
import os

# No of Attempts
game_status = True

# Clears the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_and_logo():
    clear()
    print(logo)

def random_influencer():
    '''Returns a random dictionary of data of influencer from the list'''
    # Randomly selecting the influencer
    return random.choice(data)

def check_influencer(first_influencer,second_influencer):
    '''If same influencer is randomly selected as second person then returns new influencer'''
    if first_influencer == second_influencer:
        # If the first and second influencer are randomly selected as same select a new influencer
        second_influencer = random_influencer()
        # Checking if again the same influencer are selected
        check_influencer(first_influencer,second_influencer)
    else: 
        return second_influencer

def compare(high_follower, low_follower):
    '''Takes user's high_follower Dict as first parameter and low_follower Dict as second parameter  and Returns Boolean for game status '''
    # According to the choice made by user
    high_follower_count = high_follower["follower_count"]
    low_follower_count = low_follower["follower_count"]

    if high_follower_count >= low_follower_count:
        if high_follower_count == low_follower_count:
            # print("Same Number of Followers...............")
            return True 
        # print("Game Continues..............................")
        return True
    else:
        # print("Game Ends !!!!!!!!!!!!!!!!!!!!!!")
        return False
    
def user_choice(first_influencer,second_influencer):
    '''Parameter are the first_influencer and second_influencer calls compare() and finally returns game_status as Boolean '''
    while True:
        choice = input("Who has more followers? Type 'A' or 'B' : ").upper()
        if choice == 'A':
            # print("Choice A")
            
            # User thinks high number of follower is first_influencer
            game_status=compare(first_influencer, second_influencer)
            return game_status
        elif choice == "B":
            # print("Choice B")

            # User thinks high number of follower is second_influencer
            game_status = compare(second_influencer,first_influencer)
            return game_status
        else:
            print("Enter between 'A' and 'B'")


# MAIN Game Start
clear_and_logo()

total_data = len(data)
print(f"Total data of people {total_data}")

# Data of CURRENT person VS COMPARING person
first_influencer={}
second_influencer={}

# Randomly selecting the opening person detail
first_influencer = random_influencer()

# Score
score=0
# LOOP
while game_status:
    
    # Current person Detail
    print(f"Compare A :: {first_influencer["name"]}, {first_influencer["description"]}, from {first_influencer["country"]}, followers {first_influencer["follower_count"]}")

    # ASCII VS art
    print(vs)

    # Selecting the opponent next person
    second_influencer=random_influencer()
    # Check for first and second influencer being the same
    second_influencer = check_influencer(first_influencer,second_influencer)

    # Against person Detail
    print(f"Against B :: {second_influencer["name"]}, {second_influencer["description"]}, from {second_influencer["country"]}, followers {second_influencer["follower_count"]}")

    # User prompt to select between the two option return Boolean
    game_status = user_choice(first_influencer,second_influencer)

    # Right condition returns True
    if game_status:
        # Same number of follower'score
        if first_influencer["follower_count"] != second_influencer["follower_count"]:
            score+=1
        
        clear_and_logo()
        print(f"You are right !! Current Score is: {score}")
    else:
        clear_and_logo()
        print(f"Thats wrong answer. Final Score is: {score}")
    
    first_influencer = second_influencer





