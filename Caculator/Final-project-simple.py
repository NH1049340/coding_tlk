import math

# 🔢 List of math operations
operation_names = [
    "Add", "Subtract", "Multiply", "Divide", "Square Root", "Power",
    "Minimum", "Maximum", "Modulus", "Even or Odd", "Absolute Value",
    "Area of Circle", "Celsius to Fahrenheit", "Percentage", "Factorial",
    "Multiplication Table"
]

# 📋 Function to show the list
def show_operations():
    print("🧾 Available Operations:")
    for i, name in enumerate(operation_names, start=1):
        print(f"{i}. {name}")

# 🎉 Welcome message
print("👋 Hello! Welcome to your Super Easy Calculator 🧮")
print("Let’s do all kinds of math, step by step! 🐾")

# 🌀 Main loop to keep the calculator running
while True:
    show_operations()  # ✅ Only showing this
    print("0. Exit")    # ✅ Exit option manually added

    choice = input("👉 Your choice: ")

    # 🛑 Exit condition
    if choice == "0":
        print("👋 Thank you! Goodbye!")
        break

    # 📥 For most operations, take two numbers as input
    if choice in ["1", "2", "3", "4", "6", "7", "8", "9", "14"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

    # ➕ Addition
    if choice == "1":
        print(f"Result: {a + b}")
    elif choice == "2":
        print(f"Result: {a - b}")
    elif choice == "3":
        print(f"Result: {a * b}")
    elif choice == "4":
        if b == 0:
            print("⚠️ You can't divide by zero!")
        else:
            print(f"Result: {a / b}")
    elif choice == "5":
        num = float(input("Enter a number: "))
        if num < 0:
            print("⚠️ No square root for negative numbers.")
        else:
            print(f"Square root: {math.sqrt(num)}")
    elif choice == "6":
        print(f"Power result: {math.pow(a, b)}")
    elif choice == "7":
        print(f"Minimum is: {min(a, b)}")
    elif choice == "8":
        print(f"Maximum is: {max(a, b)}")
    elif choice == "9":
        print(f"Remainder: {a % b}")
    elif choice == "10":
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("It's EVEN.")
        else:
            print("It's ODD.")
    elif choice == "11":
        num = float(input("Enter a number: "))
        print(f"Absolute value is: {abs(num)}")
    elif choice == "12":
        radius = float(input("Enter radius of the circle: "))
        print(f"Area is: {math.pi * radius * radius}")
    elif choice == "13":
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
    elif choice == "14":
        print(f"{a}% of {b} = {(a / 100) * b}")
    elif choice == "15":
        num = int(input("Enter a number: "))
        if num < 0:
            print("⚠️ Factorial not defined for negative numbers.")
        else:
            print(f"Factorial of {num} is {math.factorial(num)}")
    elif choice == "16":
        num = int(input("Enter a number: "))
        print(f"📊 Multiplication Table for {num}")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    else:
        print("❗ Invalid choice. Try again!")

    print("✅ Done! Let's do another one...")