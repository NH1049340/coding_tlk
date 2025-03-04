print("Hello,i am Noor")
print("welcome to temperature advice")
print("please enter your temperature")
temp=int(input("enter your temperature: "))
if temp<10:
    print("it is cold outside, please wear warm clothes")
elif 10 <= temp <= 25:
    print("The weather is nice, Wear short-sleeved shirts!")
elif temp > 25:
    print("It is hot outside, Stay cool!")
