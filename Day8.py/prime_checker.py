def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime Number")
    else:
        print("Not prime number")
n = input("Enter any number: ")
num = int(n)
prime_checker(num)

#prime number are having remainder only 0 when it is divided by 1 and itself. Thus, the condition is applied to check only if the number is prime or not. That's all.


    
            