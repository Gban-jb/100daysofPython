#step 4 
import random
def deal_cards():
    """ Returns a new card each time"""
    cards = [ 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#step5
#taking random 2 cards for both computer and person.

user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if user_score == 0 or computer_score == 0 or user_score > 21: 
    is_game_over = True

    
#User6 
# create a function called calculate_score() that takes a list of cards as input and returns its sum.
def calculate_score(cards):
    return sum(cards)

#Step 7
#inside calculate_score(), check for a blackjack ( a hand with only 2 cards: ace + 10)
# and returns 0 instead of the actual score. 0 will represent a blackjack in our game. 
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

 #step 8g
 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# step 9


     
     



    