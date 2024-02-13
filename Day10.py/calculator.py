def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2): 
    return n1 * n2

def div( n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

def calculator():
    num1 = float(input("Enter the first number? "))
    for symbol in operations: 
        print(symbol)
        should_continue = True
            
    while should_continue:
        operation_symbol = input("Pick an operation symbol")
        num2 = float(input("Enter the second number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' if you want to continue {answer}, or type 'n' if you want to start new: ") == 'y': 
            num1 = answer
        else: 
            should_continue = False
            calculator()      
calculator()

        
        