print("Sum of even numbers between the particular number")

user_number = input("Enter any number: ");
num = int(user_number)
total = 0

if num % 2 == 0:
    for even in range(0, num+1, 2):
        total += even
    print(f"THe sum is {total}")
    
else:
    num_2 = num + 1
    for even2 in range(0, num_2, 2):
        total += even2
    print(f"The sum is {total}.")