from ascii_art import calculator_art

ascii_art = calculator_art()
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-" : sub,
    "/" : divide,
    "*" : multiply
}

#acces the key to use the operation and how to use the function 
# result = operations["*"](4, 8)
# print(result)
print(calculator_art)

def calculator():
    should_continue = True
    n1 = float(input("Type your first number here: "))

    while should_continue: 

        for symbol in operations:
            print(symbol)
            
        operation_symbol = input("Type your operation choice: ")
        n2 = float(input("Type your second number here: "))
        answer = (operations[operation_symbol](n1, n2))
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        choice = input(f"Type 'y' to continue with {answer} or type 'n' to start again: ")

        if choice == "y":
            n1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator() # using recursion to keep playing 

calculator()