import os
import art

# Function to perform addition operation
def add(n1 , n2):
    return n1 + n2

# Function to perform a subtraction operation
def subtraction(n1 , n2):
    return n1 - n2

# Function to perform multiplication operation
def multiplication(n1, n2):
    return n1 * n2

# Function to perform division operation
def division(n1, n2):
    return n1 / n2

# Function to find the remainder after division
def remainder(n1, n2):
    return n1 % n2

# Function to perform exponentiation operation
def power(n1, n2):
    return n1 ** n2

# Dictionary containing supported mathematical operations
operations = {
    "+": add,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "%": remainder,
    "^": power
}

# Main calculator function
def math():
    """
    A simple calculator function that takes user input for numbers and operations,
    performs the calculation, and prints the result.
    """
    
    print(art.logo)
    num1 = input("First number:\n")
    
    if num1.isnumeric():
        loop = 'y'
        num1 = float(num1)
        
        for i in operations:# shows the user all the operations.
                print(i)
        
        while loop == 'y':
            symbol = input("what operation do you want:\n")
            
            if symbol in operations:  # Check if the symbol is supported
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
                        math()  # Recursive call to restart the calculator
                        
                else:
                    os.system('cls')
                    print(f"'{num2}' is not a number.")
                    math()  # Recursive call to restart the calculator
                    
            else:
                os.system('cls')
                print(f"This symbol '{symbol}' is not recognized by the calculator, please try calculating again.")
                math()  # Recursive call to restart the calculator
                
    else:
        os.system('cls')
        print(f"'{num1}' is not a number.")
        math()  # Recursive call to restart the calculator

math()  # Start the calculator
