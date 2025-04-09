# -----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Noor ul haq
# Created:     20-Mar-2025
# Updated:     25-Mar-2025
# -----------------------------------------------------------------------------
# Create the list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Create a list of squared numbers from the even_numbers list
squared_numbers = [num * num for num in even_numbers]

# Print both lists
print("Even Numbers:", even_numbers)
print("Squared Numbers:", squared_numbers)