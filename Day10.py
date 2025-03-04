adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

squared = 5**2
print(squared)

modulo = 15 % 4
print(modulo)

divisor = 15 // 4
print(divisor)

# new section round(varible name , decimal places)
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)