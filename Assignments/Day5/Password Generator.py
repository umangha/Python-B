#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

########################################## MY WAY ##########################################

# ## Easy Level Order not randomised

# ## For holders for letter, symbol and numbers
# letters_holder=''
# symbols_holder=''
# num_holder=''
# holder=''

# # Calculating the length of the list and subtracting 1 as the total length is not in index
# length_letters=len(letters)-1
# length_symbols=len(symbols)-1
# length_num=len(numbers)-1


# # Loop for letter
# for i in range(0,nr_letters):
#     rand_i=random.randint(0,length_letters)
#     letters_holder+= letters[rand_i]


# # Loop for Symbols
# for i in range(0,nr_symbols):
#     rand_i=random.randint(0,length_symbols)
#     symbols_holder+=symbols[rand_i]

# # Loop for numbers
# for i in range(0,nr_numbers):
#     rand_i=random.randint(0,length_num)
#     num_holder+=numbers[rand_i]

# holder=letters_holder+symbols_holder+num_holder

# print("Password generated is: ",holder)

# #############################################################################

# ## Randomising the order as well 

# # Finding the length of the final holder containing output and subs 1 to not get array out of index error
# len_holder=len(holder)-1

# # Holds the random output
# randomized_holder=''

# for i in range(0,len_holder):
#     rand_i=random.randint(0,len_holder)
#     randomized_holder+=holder[rand_i]

# print("Randomized Out of order Password generated is: ",randomized_holder)


###################################### Alternative Way #######################################

# In Order
# Creating a list for password
password=[]

for char in range(0,nr_letters):

    # Syntax :: random.choice(mylist)
    password+= random.choice(letters)

for symbol in range(0,nr_symbols):
    password+= random.choice(symbols)

for number in range(0,nr_numbers):
    password+= random.choice(numbers)

print("\nBefore Shuffle: ",password)

random.shuffle(password)

print("\nAfter Shuffle: ",password)

# Final password holder
shuffle_pw=''

# Looping the password list to get string value
for i in password:
    shuffle_pw+=i

print("\nFinal Randomized Password :", shuffle_pw)