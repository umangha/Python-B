# Inital Hello print
print("Welsome to the tip calculator!")

#Ask the total bill
bill=float(input("What was the total bill? $ "))

#percentage of tip offered
tip_per=float(input("How much tip would you like to give? 10, 12, or 15? "))


# Number of people to split the bill
no_of_people=int(input("How many people to split the bill? "))

# tip money
tip=bill*(tip_per/100)

# total payable amount
total_bill=bill + tip

#Individual money with 2 decimal point
individual_bill = round(total_bill/no_of_people,2)

print(f"Each person should pay: ${individual_bill}")


