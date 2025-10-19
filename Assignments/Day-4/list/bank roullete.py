

# Number of names in the list
no_names=len(names)

# Randomly selecting a number between 0 and 4
random_payer=random.randint(0, no_names-1)

# Payer name
payer=names[random_payer]
print(payer + " is going to buy the meal today!")