# import random

# letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']
# number = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbol = ['@', '#', '!', '$','%', '&', '*']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("Enter how many letters you like to add\n"))
# nr_symbols = int(input("Enter how many symbols you like to add\n"))
# nr_number = int(input("Enter how many number you like to add\n"))

# password = ""
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letter)
#     password = password + random_char
#     first = password

# for sym in range(1, nr_symbols + 1):
#     random_sym = random.choice(symbol)
#     password += random_sym
#     second = password

# for numb in range(1,  nr_number +1):
#     random_numb = random.choice(number)
#     password += random_numb
#     third = password
    
# print(f"Your simple passwordd is this: {password}")

# final = first + second + third
# password_final = random.choices(final)

# print(f"Your complex password is {password_final}")



import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']
number = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['@', '#', '!', '$','%', '&', '*']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("Enter how many letters you like to add\n"))
nr_symbols = int(input("Enter how many symbols you like to add\n"))
nr_number = int(input("Enter how many number you like to add\n"))

password_list = []
for char in range(1, nr_letters + 1):
    random_char = random.choice(letter)
    password_list += random_char

for sym in range(1, nr_symbols + 1):
    random_sym = random.choice(symbol)
    password_list += random_sym

for numb in range(1,  nr_number +1):
    random_numb = random.choice(number)
    password_list += random_numb
    
    random.shuffle(password_list)
    
    print(password_list)
    
    password = ""
    for char in password_list:
        password += char

print(f"Your Final HArd Password is : {password}");

    