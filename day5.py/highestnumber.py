print("The program for finding the highest number")
student_mark = input("Enter the different marks ").split()

for n in range(0, len(student_mark)):
    student_mark[n] = int(student_mark [n])

highest_score = 0
for score in student_mark:
    if score > highest_score:
        highest_score = score

print(f"THe highest score of the above scores is {highest_score}.")

    

    
    
