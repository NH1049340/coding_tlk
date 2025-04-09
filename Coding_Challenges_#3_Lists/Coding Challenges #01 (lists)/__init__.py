#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Noor ul haq
# Created:     20-Mar-2025
# Updated:     25-Mar-2025
#-----------------------------------------------------------------------------

# Create the list of students
students = [['Alice', 25, 'Physics'], ['Bob', 22, 'Chemistry'], ['Charlie', 24, 'Biology']]

# Update Bob's age and major
students[1] = ['Bob', 23, 'Mathematics']

# Print the updated students list
print(students)

# Find and print the name of the student studying 'Biology'
for student in students:
    if student[2] == 'Biology':
        print(student[0])