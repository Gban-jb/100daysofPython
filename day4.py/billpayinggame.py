print("Welcome to the Bill Paying Game between your friends.")
Name_List = ["Jeeban", "Bishal", "Suyog", "Prasanna", "Sumit", "Aayush", "Dipesh", "Anam", "James", "John", "Hrig", "Kabins B.", "Jebs"]

import random
name = random.choice (Name_List);

decision = input("The results is ready to go. Do you want to know the result. Yes or No?").lower()
if decision == 'yes':
    print(f"{name}, is going to buy the meal today!");
else: 
    print("Alright! Discuss and decide soon if you want to play!");
    
