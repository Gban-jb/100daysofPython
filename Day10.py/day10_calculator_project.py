def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator(): 
    num1 = int(input("Enter the first number? "))
    for symbols in operation:
        print(symbols)
    
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation? ")
        num2 = int(input("Enter the second number? "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"The answer of the {num1}, {operation_symbol} {num2} = {answer}")
        
        if input("DO you want to continue from the last answer, then type 'y', else want to begin from the start type'n'") =='y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()



