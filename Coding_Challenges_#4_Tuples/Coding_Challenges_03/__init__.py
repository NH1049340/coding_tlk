# Create a tuple with repeated values
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Ask the user to enter a fruit name
user_input = input("Enter a fruit name: ")

# Print how many times that fruit appears in the tuple
count = fruits.count(user_input)
print(f"The fruit '{user_input}' appears {count} time(s) in the tuple.")