print("Let's find out the Leap Year!");
year = int(input("Enter the year: "));
print("Is it cleanly divisible by 4?");
if year % 4 ==0:
    print("yeah, it is divisible by 4.");
    print("Is it cleanly divisible by 100?");
    if year % 100 ==0:
        print("yeah, it is divisible by 100.");
        print("Is it cleanly divisible by 400?");
        if year % 400 ==0:
            print("Yes, it is divisible by 400.");
            print("It is a leap year!");
        else: 
            print("This is not divisible by 400.");
            print(" It is not a leap year!");
    else:
        print("No, it is not divisible by 100.");
        print("Yet! This is a leap year, man!");
else:
    print("Ohhh No! It is not divisible by 4.");
    print("This is not a leap year boy/girl!");
    
    