print("Welcome to the Tip Calculator!");
bill = float(input("What was the total bills? $"));
tip = int(input("How much tip you going to give up? 10, 12 or 15?"));
people = int(input("How many people you are going to split from?"));
bill_with_tip = ((bill * (1 + tip /100)));

people_spliting = bill_with_tip / people
final_amount = round(people_spliting, 2);
print(f"The bill is to the { final_amount} per person.");