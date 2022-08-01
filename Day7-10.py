# simple calculator but with a small tweak the previous calculation can be continued
def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

operations = {
    '+' : add,
    '-' : subtract,
    '/' : divide,
    '*' : multiply
}

num1 = int(input("What's the first number? : "))
num2 = int(input("what's the second number? :"))

[print(x) for x in operations.keys()]

operation_symbol = input("Pick an operation from live above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)
print(f"The result is\n\n {answer}")
is_continued = True
while is_continued:
    if input(f"Type 'y' for continuing with {answer} and 'n' for exit: ") == 'y':
        num1 = answer
        num2 = int(input("What's the second number? : "))
        [print(x) for x in operations.keys()]
        operation_symbol = input("Pick an operation from live above: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"The result is\n\n {answer}")
    else:
        is_continued = False

    