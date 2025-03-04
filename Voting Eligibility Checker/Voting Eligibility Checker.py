# ask the user to enter their age
print("Welcome to the Voting Eligibility Checker App!")
# Store the age in a variable
age = int(input("enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
# Use conditional statements to check if the person is eligible to vote
else:
    print("Sorry, You are not eligible to vote!")