#Step 4

import random

# Use r to use as raw text and not get that escape syntax error
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives=6


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Flag for finding whether the guess was correct or not
    guess_correct=False 

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            guess_correct=True

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess_correct==False:
      lives-=1

    # Game Over When Lives hit 0
    if lives<0:
      end_of_game=True
      print("Game Over")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if lives>=0:
      print(stages[lives])