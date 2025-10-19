rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

##########################################

import random

#creating a list of rock , paper and scissors
options=[rock,paper,scissors]

# Enter 0 1 or 2
user=int(input("Enter 0 for rock, 1 for paper and 2 for scissor: "))

# Randomly selecting the options for computer
computer=random.randint(0,2)

# Error validating for wrong input by user
if user >=3 or user <0:
    print("Enter valid Choice from 0 for rock, 1 for paper and 2 for scissor!!!")
else:

    # User Choice
    print("User's Choice: \n",options[user])

    # Computer Choice
    print("Computer's Choice:\n",options[computer])

    # Using If-else condition cause i couldnot think how i will use loop in this
    # Flag to check the win=1, lose=-1 and draw=0 condition
    condition=0

    # if else start
    if user==0:
        if computer==0:
            # Draw
            condition=0
        elif computer==1:
            # Lose
            condition=-1
        else:
            # Win
            condition=1
    elif user==1:
        if computer==0:
            # Win
            condition=1
        elif computer==1:
            # Draw
            condition=0
        else:
            # Lose
            condition=-1
    elif user==2:
        if computer==0:
            # Lose
            condition=-1
        elif computer==1:
            # Win
            condition=1
        else:
            # Draw
            condition=0

    # Checking the status of the game and printing the result
    if condition==0:
        print("Draw")
    elif condition==1:
        print("You Win!")
    else: 
        print("You Lose!!")