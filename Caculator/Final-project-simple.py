import math

# 🎉 Welcome message
print("👋 Hello! Welcome to your Super Easy Calculator 🧮")
print("Let’s do all kinds of math, step by step! 🐾")

# 🌀 Main loop to keep the calculator running
while True:
    # 📋 Show menu options
    print("📚 Choose one of these options:")
    print("1️⃣  Add")
    print("2️⃣  Subtract")
    print("3️⃣  Multiply")
    print("4️⃣  Divide")
    print("5️⃣  Square Root")
    print("6️⃣  Power (x^y)")
    print("7️⃣  Find Minimum")
    print("8️⃣  Find Maximum")
    print("9️⃣  Remainder (Modulus)")
    print("🔟  Check Even or Odd")
    print("1️⃣1️⃣  Absolute Value")
    print("1️⃣2️⃣  Area of a Circle")
    print("1️⃣3️⃣  Celsius to Fahrenheit")
    print("1️⃣4️⃣  Percentage")
    print("1️⃣5️⃣  Factorial")
    print("1️⃣6️⃣  Multiplication Table")
    print("0️⃣  Exit")

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
    # ➖ Subtraction
    elif choice == "2":
        print(f"Result: {a - b}")
    # ✖️ Multiplication
    elif choice == "3":
        print(f"Result: {a * b}")
    # ➗ Division with zero check
    elif choice == "4":
        if b == 0:
            print("⚠️ You can't divide by zero!")
        else:
            print(f"Result: {a / b}")
    # 🟰 Square root
    elif choice == "5":
        num = float(input("Enter a number: "))
        if num < 0:
            print("⚠️ No square root for negative numbers.")
        else:
            print(f"Square root: {math.sqrt(num)}")
    # ⬆️ Power (x^y)
    elif choice == "6":
        print(f"Power result: {math.pow(a, b)}")
    # 🔽 Minimum
    elif choice == "7":
        print(f"Minimum is: {min(a, b)}")
    # 🔼 Maximum
    elif choice == "8":
        print(f"Maximum is: {max(a, b)}")
    # ➗ Modulus (remainder)
    elif choice == "9":
        print(f"Remainder: {a % b}")
    # 🔍 Even or Odd
    elif choice == "10":
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("It's EVEN.")
        else:
            print("It's ODD.")
    # 📏 Absolute value
    elif choice == "11":
        num = float(input("Enter a number: "))
        print(f"Absolute value is: {abs(num)}")
    # 🟢 Area of a circle
    elif choice == "12":
        radius = float(input("Enter radius of the circle: "))
        print(f"Area is: {math.pi * radius * radius}")
    # 🌡️ Celsius to Fahrenheit
    elif choice == "13":
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
    # 📉 Percentage
    elif choice == "14":
        print(f"{a}% of {b} = {(a / 100) * b}")
    # 🔢 Factorial
    elif choice == "15":
        num = int(input("Enter a number: "))
        if num < 0:
            print("⚠️ Factorial not defined for negative numbers.")
        else:
            print(f"Factorial of {num} is {math.factorial(num)}")
    # 🧮 Multiplication table
    elif choice == "16":
        num = int(input("Enter a number: "))
        print(f"📊 Multiplication Table for {num}")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    else:
        print("❗ Invalid choice. Try again!")

    print("✅ Done! Let's do another one...")