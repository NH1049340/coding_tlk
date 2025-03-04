#Ask the user to enter a number.
print("Hello, Welcome back to Even or Odd Number Checker "
      "are you ready?")
#Store the number in a variable.
ready = input("Are you ready? (yes/no): ")
# Use conditional statements to check if the number is even or odd.
if ready == "yes":
    print("Great! Let's proceed.")
if int(input("Enter your number: ")) % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")