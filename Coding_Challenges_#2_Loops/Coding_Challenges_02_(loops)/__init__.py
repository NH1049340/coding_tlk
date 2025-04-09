#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Noor ul haq
# Created:     01-Mar-2025
# Updated:     15-Mar-2025
#-----------------------------------------------------------------------------

import random
random_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10. Can you guess it?")
user_guess = 0
# Use a while loop to keep running until the guess is correct
while user_guess != random_number:
    # Ask the user to make a guess
    user_guess = int(input("Enter your guess: "))
    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
else:
        print('Correct! You win! 🎉')
