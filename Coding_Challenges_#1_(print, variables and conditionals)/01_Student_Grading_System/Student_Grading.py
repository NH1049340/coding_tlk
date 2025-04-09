print('Hello, i am noor')
print("Welcome to my Student Grading System")
# Ask the user to enter their score (out of 100)
print("Please enter your score between 0 and 100")
# Store the score in a variable
myScore = int(input("Enter your score: "))
# Use conditional statements to print the grade based on the score
if myScore >= 90: # 90 to up ...
    print("Grade: A")
    print("Congratulations, you are successful!")
elif myScore >= 80:  # 80 to 89
    print("Grade: B")
    print("Congratulations, you are successful!")
elif myScore >= 70:  # 70 to 79
    print("Grade: C")
    print("Congratulations, you are successful!")
elif myScore >= 50:  # 50 to 69
    print("Grade: D")
    print("Congratulations, you are successful!")
elif myScore > 49:  # 0 to 49
    print("Fail. Try next time")
print("Do you have any question? 🤔")
