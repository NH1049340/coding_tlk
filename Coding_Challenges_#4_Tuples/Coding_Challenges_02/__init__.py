# Ask the user to input two numbers
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

# Swap the values using tuple unpacking
first_number, second_number = second_number, first_number

# Print the swapped values
print(f"Swapped values: ({first_number}, {second_number})")