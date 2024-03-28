#display art
import random
from art import logo
from game_data import data

#Generate the random account from the game data
a_number = random.choice(data)
print(a_number)
b_number = random.choice(data)
if a_number == b_number:
    b_number = random.choice(data)

print(b_number)
#Format the account data into printable format

def format_data(account):
    """ Format the account into the printable form """
    account_name = account["name"]
    account_follower = account["follower"]
    account_desc = account["description"]
    account_country = account["country"]
    
    return (f"{account_name}, have {account_follower} follower, from {account_country} and field of {account_desc}")
    

#Ask user for a guess
print(logo)
 
# Check if user is correct
#Get follower count of each account.
#Use if statement to check if user is correct.

#Give user feedback on their guess.

#Score keeping

#Keep the game repeatable

#Making account  at position B become the next account at position A.

#Clear the screen between the rounds.
