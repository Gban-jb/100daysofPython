import os
def clear():
    os.system('clear')
    
from art import logo

print(logo)
bids= {}

def find_highest_bid(bidding_record): 
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        #bidding_record = {"Angela" : 123, "Jeeban": 321}
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, and the bidding amount is {highest_bid}")
    
    
biding_finished = False

while not biding_finished: 
    name = input("Enter the Name:")
    price = int(input("What is your biding price? $"))
    bids[name] = price #..................

    should_continue = input("Are there any person who want to continue? If yes type'yes', else type 'no' ")
    if should_continue == "no":
        biding_finished = True
        find_highest_bid(bids)
    elif should_continue =="yes":
        clear()
    

