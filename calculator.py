"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

# repeat forever:
while True:
    # read input
    user_input = input("What is your equation? ")

    # tokenize input
    tokens = user_input.split(' ')

    # if the first token is "q":
    if "q" in tokens:
        print("Quit, you will now exit.")
        # break out of the loop which quits the script          
        break

    # if tokens contains 0 or 1 item
    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue
    
    # operator variable
    operator = token[0]
    # num1 variable
    num1 = tokens[1]
    
    # if using square or cube, num2 is not provided
    if len(tokens) < 3:
        num2 = "0"

    # in most cases, the user provides a 2nd num
    else:
        num2 = tokens[2]

    
    # if len(tokens) > 3:
    #     num3 = tokens[3]

    # A place to store the return value of the math function we call,
    # to give us one clear place where that result is printed.
    result = None

    # Check if user input for num1 and num2 are numbers
    if not num1.isdigit() or not num2.isdigit():
        print("Those aren't numbers!")
        continue

    num1 = float(num1)
    num2 = float(num2)

    # (decide which math function to call based on first token)
    # if the first token is '+':
    elif operator == "+":
        # call the add function with the other two tokens
        result = add(num1, num2)

    # if the first token is '-':
    elif operator == "-":
        # call the subtract function with the other two tokens
        result = subtract(num1, num2)

    # if the first token is '*':
    elif operator == "*":
        # call the multiply function with the other two tokens
        result = multiply(num1, num2)

    # if the first token is '/':
    elif operator == "/":
        # call the divide function with the other two tokens
        result = divide(num1, num2)

    # if the first token is 'square':
    elif operator == "square":
        # call the square function with the other two tokens
        result = square(num1)

    # if the first token is 'cube':
    elif operator == "cube":
        # call the cube function with the other two tokens
        result = cube(num1)

    # if the first token is 'pow':
    elif operator == "pow":
        # call the power function with the other two tokens
        result = power(num1, num2)

    # if the first token is 'mod':
    elif operator == "mod":
        # call the mod function with the other two tokens
        result = mod(num1, num2)
    
    # if incorrect items entered
    else:
        result = "Please enter an operator followed by two integers."
    
    print(result)