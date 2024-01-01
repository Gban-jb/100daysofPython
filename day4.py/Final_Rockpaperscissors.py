print("Welcome to the Playhouse")

import random

rock = "Rock Image"
paper = "Paper Image"
scissors = " Scissors Image"
game_images = [rock, paper, scissors]

user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"));

if user_choice >= 3 or user_choice < 0 :
    print(f"You lose as this number is invalid. {user_choice}")
else:  
    print(f" Your image is : {game_images[user_choice]}");

    computer_choice = random.randint(0, 2)
    print(f"Computer Choice is {computer_choice} It's image is: ")
    print(game_images[computer_choice]);    

    if user_choice == 0 and computer_choice ==2:
        print("You won! As Rock Beats Scissors!")
    elif computer_choice == 0 and user_choice ==2:
        print("You Lose!")
            
    elif computer_choice > user_choice:
        print("Computer win, you lose!")
    elif user_choice > computer_choice:
        print("You won!")
            
    elif computer_choice == user_choice:
        print("Its a Draw!")
    