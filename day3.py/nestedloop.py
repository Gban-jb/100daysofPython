print("Welcome to the Nested Loop Learning!");
height = int(input("Enter your height: "))
bill = 0
if height >= 120:
    print("Yeah, we can ride the Rollercoaster");
    age = int(input("Enter your age: "));
    if age <= 12:
        bill = 10;
        print(f"Your age is {age}");
    elif 50 > age > 12:
        bill = 20;
        print(f" Your age is {age}");
    else:
        bill = 15;
        print("Pay $15.");
    photos = input("Do you want to take photos? Y or N?");
    if photos =='Y':
        bill += 3
        print(f"Your total bill is {bill}")
    
    else: 
        print(f"Your total bill is {bill}")
else:
    print(f"Ohh! Your height is {height}, You are not elligible to ride the Rollercoaster.")
    