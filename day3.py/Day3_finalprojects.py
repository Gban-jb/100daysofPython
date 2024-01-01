print("Welcome to the Treasure Island!");
print("Your mission is to find the treasure.");

choice1 = input("Where do you want to go? Left or Right ").lower()

if choice1 == "left":
    choice2 = input("Congratulations, you passed this steps. Now you are in the centre of the big ponds. Do you want to wait for the boat or swim and get out. type 'wait' for waiting and 'swim' for swimming ").lower()
    if choice2 == "wait":
        choice3 = input("You play so well. Now you are at the hall and there is three doors. Which one would you like to go and take rest! Type 'Red' for first one, type 'yellow' for second one and 'blue' for third one ").lower();
        if choice3 == "red":
            print("Game Over! There is a big snake, you can't sleep there!")
            
        elif choice3 == "yellow":
            print("Hurray! You won the game! Congratulations!")
        else:
            print("Oh bad day! The room is already occupied! Game Over");
    else:
        print("The  big shark killed you. Game over!");
    
    
    
else:
    print("You fell into a hole. Game over!")
