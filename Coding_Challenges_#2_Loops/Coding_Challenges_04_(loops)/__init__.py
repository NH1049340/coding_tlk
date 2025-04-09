#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Noor ul haq
# Created:     01-Mar-2025
# Updated:     15-Mar-2025
#-----------------------------------------------------------------------------

# Countdown from 10 to 1 with "stop" functionality
for num in range(10, 0, -1):
    print(num)
    user_input = input("Enter 'stop' to break the countdown or press Enter to continue: ").strip().lower()
    if user_input == "stop":
        print("Countdown stopped by user.")
        break
else:
    print("Countdown completed.")


