import os

# Clears the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# List holding all the dictionary
bidding_list=[]

# Inserting new bidder info as dictionary in List
def bidding_detail(bidder_name,final_bid):
    bidding_list.append({
        "name":bidder_name,
        "bid":final_bid
    })


# finding winner
def winner():
    for index in bidding_list:
        # print(index)
        winning_bid=0
        winning_bidder=''
        # "index" here represents the 1 dictionary of the list biddint_list
        current_bidder=index["name"]
        current_bid=index["bid"]
        if winning_bid<current_bid:
            winning_bid=current_bid
            winning_bidder=current_bidder

    return {
            "name":winning_bidder,
            "bid": winning_bid
        }
        


# Asking input from  User until they answer "no"
# Continuation Status
status=True

# Loop infinitely till True
while status:
    name=input("Enter Your Name: ")
    bid=int(input("Enter Your Bid: "))
    # Inserting the info in the List in the form of dictionary
    bidding_detail(bidder_name=name,final_bid=bid)


    more_bidders=input("Are there more bidders? yes or no ")
    # Exit the loop
    if more_bidders=="no":
        status=False
    clear()

# Outside the infinite while loop 
# Returns a dictionary with winner name and bid
winner_dict= winner()

print(f"{winner_dict["name"]} is the winner with winning bid of {winner_dict["bid"]}$")