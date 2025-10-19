#Step 5

import random
from hangman_art import *
from hangman_words import *

# To clear screen after each asking time
import os

# Choosing a random word from the handman_words file
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# end game status
end_of_game = False

# lives in the game
lives = 6

# Just prints the logo of hangman
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    # Asking for guess of the user
    guess = input("Guess a letter: ").lower()

    # Clearing the Screen
    os.system('cls')

    # Check if User has already guessed the number
    if guess in display:
        print(f"\nYOU HAVE ALREADY GUESSED  {guess} !!")
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"\nYou guess {guess} is incorrect.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Hangman Image status
    print(stages[lives])