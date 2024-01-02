print("Average Height");
sum = 0
height = input("Enter all the heights: ").split()

for n in range(0, len(height)):
    height[n] = int(height[n]);
    sum += height[n]
print(f" The total sum of the entered height is {sum}. ");

students_number = len(height)
print(f"The total number of students is {students_number}")

average = int (sum / students_number)
print(f" The average sum of the above height is {average}.")
    
    

