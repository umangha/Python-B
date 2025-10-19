# Build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

#######################################################
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

##########################################################

# tracking total amount of the bill
bill=0

# First Condition for the size of Pizza S, M, L
if size=='S':
    bill+=15
elif size=='M':
    bill+=20
elif size=="L":
    bill+=25
else:
    print("Enter the Pizza Size: S, M, L")

# If pepperoni is selected to be used
if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    elif size=="M" or "L":
        bill+=3

# Extra cheese for any size pizza
if extra_cheese=="Y":
    bill+=1

print(f"Your final bill is: ${bill}.")