import os
import art
def add(n1 , n2):
    return n1 + n2

def subtraction(n1 , n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def reminder(n1, n2):
    return n1 % n2
def power(n1, n2):
    return n1 ** n2

operations = {
    "+": add,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "%": reminder,
    "^": power
}
def math():
    print(art.logo)
    num1 = input("First number:\n")
    if num1.isnumeric():
        loop = 'y'
        num1 = float(num1)
        for i in operations:
                print(i)
        
        while loop == 'y':
            symbol = input("what operation do you want:\n")
            if symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/" or symbol == "^" or symbol == "%":
                num2 = input("next number:\n")
                if num2.isnumeric():
                    num2 = float(num2)
                    answer = operations[symbol](num1, num2)
                    print(f"The result of the calculation is,\n{num1} {symbol} {num2} = {answer}")

                    loop = input("Input 'y' to do more calculations with the previous answer or 'n' to start a new calculation.\n")

                    if loop == 'y':
                        num1 = answer
                    else:
                        os.system('cls')
                        math()
                else:
                    os.system('cls')
                    print(f"'{num2}' is not a number.")
                    math()
            else:
                os.system('cls')
                print(f"This symbol '{symbol}' is not recognized by the calculator,pleas try calculating again.")
                math()
    else:
        os.system('cls')
        print(f"'{num1}' is not a number.")
        math()

math()