#Step 1 

word_list = ["aardvark", "baboon", "camel"]


###################################################################################################
import random

# Randomly choosing one of the word from the list
chosen_word = random.choice(word_list)

# Asking the user to enter a letter
guess= input("Enter a letter to guess: ").lower()

# looping through the choosen word
for letter in chosen_word:
    if guess[0] == letter:
        print("right")
    else:
        print("wrong")