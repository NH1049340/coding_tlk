print("Hello,i am Noor")
print("welcome to temperature advice")
# Ask the user to enter the current temperature
print("please enter your temperature")
# Store the temperature in a variable
temp=int(input("enter your temperature: "))
# Use conditional statements to give advice based on the temperature
if temp<10:
    print("it is cold outside, please wear warm clothes")
elif 10 <= temp <= 25:
    print("The weather is nice, Wear short-sleeved shirts!")
elif temp > 25:
    print("It is hot outside, Stay cool!")
