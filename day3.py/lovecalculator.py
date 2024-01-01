print("Hey, Welcome to the places where we find out the bonding between your partner!");
name_1 = input("Enter your full name: ");
name_2 = input("Enter your partner's full name: ");

combined_names = name_1 + name_2
lower_names = combined_names.lower();
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e

score = str(first_digit) + str(second_digit)
score_ = int(score)

if (score_ < 10) or (score_ > 90):
    print(f"Your score is {score_}, You go together like coke and mentos");
elif(score_ >= 40) and (score_ <= 50):
    print(f"Your score is {score_}, You are already together");
elif(score_ > 50) and (score_ <= 70):
    print(f"Your score is {score_}, You can have engagements soon!");
else:
    print(f"Your score is {score_}, you better spend more time like watching movies together or going for a treking");



