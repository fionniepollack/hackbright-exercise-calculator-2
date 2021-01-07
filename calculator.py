"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code


# repeat forever:
while True:
    # read input
    user_input = input("What is your equation? ")

    # tokenize input
    tokens = user_input.split('.')

    # if the first token is "q":
    if "q" in tokens:
        print("Quit, you will now exit.")
        # quit          
        break

    # else:
    else:

#             (decide which math function to call based on first token)
#             if the first token is '+':
#                   call the add function with the other two tokens
            
#             if the first token is '-':
#                   call the subtract function with the other two tokens

#             if the first token is '*':
#                   call the multiply function with the other two tokens

#             if the first token is '/':
#                   call the divide function with the other two tokens
            
#             if the first token is 'square':
#                   call the square function with the other two tokens

#             if the first token is 'cube':
#                   call the cube function with the other two tokens
            
#             if the first token is 'pow':
#                   call the power function with the other two tokens
            
#             if the first token is 'mod':
#                   call the mod function with the other two tokens