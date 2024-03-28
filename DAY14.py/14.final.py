print("Higher_Lower_game")
import random
from game_data import data
from art import logo, vs


print(logo)
print(vs)

def get_random_account():
    """Getting the random choice from the data list."""
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return (f"{name}, a {description}, from {country}")

def check_answer(guess, a_follower, b_follower):
    """Winner winning case"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


def game():    
    print(logo)
    score = 0
    game_should_continue = True
    a_account = get_random_account()
    b_account = get_random_account()
        
    while game_should_continue:
        a_account = b_account
        b_account = get_random_account()
    
        while a_account == b_account:
            b_account = get_random_account()     
        
        print(f"Compare A: {format_data(a_account)}")
        print(vs)
        print(f"Against B: {format_data(b_account)}")
        
        guess = input("Guess who has more follower? Type A or B: ").lower()
        a_follower_count = a_account["follower_count"]
        b_follower_count = b_account["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        #clear()

    # print(logo)
        if is_correct:
            score += 1
            print(f"You are right! Your score is {score}")
        else: 
            game_should_continue = False
            print(f"You are Wrong! Your score is {score}")
            
game()
    
