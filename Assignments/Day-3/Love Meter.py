
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:
#     Take both people's names and check for the number of times the letters in the word TRUE occurs.
#     Then check for the number of times the letters in the word LOVE occurs.
#     Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."

#################################################################

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?


# Making the name Lower Case
lower_name1=name1.lower()
lower_name2=name2.lower()

# Combining Both Names in Lowercase to Check TRUE and LOVE count
combined_name=lower_name1 + lower_name2

# Calculating TRUE in the combined name
no_of_t=combined_name.count('t')
no_of_r=combined_name.count('r')
no_of_u=combined_name.count('u')
no_of_e=combined_name.count('e')
no_of_true= no_of_t + no_of_r + no_of_u + no_of_e

# Calculating LOVE in the combined name
no_of_l=combined_name.count('l')
no_of_o=combined_name.count('o')
no_of_v=combined_name.count('v')
no_of_e=combined_name.count('e')
no_of_love= no_of_l + no_of_o + no_of_v + no_of_e

# Concatinating no of times TRUE and LOVE count
true_love=int(str(no_of_true)+str(no_of_love))

# Final Condition Checker
if true_love<10 or true_love>90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love>40 and true_love<50:
    print(f'Your score is {true_love}, you are alright together.')
else:
    print(f"Your score is {true_love}.")
