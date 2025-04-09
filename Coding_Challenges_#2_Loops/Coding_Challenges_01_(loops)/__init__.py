#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Noor ul haq
# Created:     01-Mar-2025
# Updated:     15-Mar-2025
#-----------------------------------------------------------------------------

# Ask the user for a number n
n = int(input("Enter a number n: "))
# Initialize the sum variable
total_sum = 0
# Use a for loop to calculate the sum
for num in range(1, n + 1):
    total_sum += num  # Add the current number to the total sum
print(f'The sum of all numbers from 1 to {n} is: {total_sum}')