# Kera Kennedy
# 6/22/2026
# P1HW2
# Creating a program for a person to enter in information about their expenses, calculate the expenses together and then subtract it from the budget, and then have it display the results

print("This program calculates and displays travel expenses")
print()

num1 = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
num2 = int(input("How much do you think you will spend on gas? "))
num3 = int(input("Approximately, how much will you need for accomodation/hotel? "))
num4 = int(input("Last, how much do you need for food? "))

cost = num2 + num3 + num4
final_result = num1 - cost

print("--------Travel Expenses---------")

print("Location: ", destination)
print("Initial Budget: ", num1)
print()

print("Fuel: ", num2)
print("Accomodation: ", num3)
print("Food: ", num4)
print()

print("Remaining Balance: ", final_result)