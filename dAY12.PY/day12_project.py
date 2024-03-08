import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(answer, user_guess, turns):
    user_guess = int(input("Make a guess: "))
    if answer > user_guess:
            print("Too low")
            return turns -1
            #print(f"You have, {turns -1} attempts left.")

    elif answer < user_guess:
            print("Too high")
            return turns -1
            #print(f"You have, {turns -1 } attempts left.")

    else:
            print(f"You guess the right number. Wooo! Congrats and the correct number is ,{answer}")
            return turns -1
            #print(f"You have, {turns -1} attempts left.")
    

def difficulty_level():
    difficulty = input("Enter the difficulty level you wanna play, type 'easy' or ' hard'").lower()
    if difficulty == 'easy':
        return EASY_LEVEL
    elif difficulty == 'hard':
        return HARD_LEVEL
    
    
def game():
    print("Welcome to the number guessing game!")
    print("I am choosing from 1 to 100.")
    answer = random.randint(1, 100)
    user_guess = 0
    turns = difficulty_level()
    while answer != user_guess:
        print(f"You have {turns} remaining to guess the number.")
        
        user_guess = int(input("Make a guess: "))
        
        turns = check_answer(answer, user_guess, turns)
        if turns == '0':
            print(f"You have run out of the moves, you lose!")
            return
        elif user_guess != answer:
            print("Guess again!")
            
game()
                