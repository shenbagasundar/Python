# Python program for simple calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2


print("Please select (1) for add and (2) for Sub")

# Take input from the user
select = input("Select operations form 1, 2 :")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == '1':
    print(add(number_1, number_2))

elif select == '2':
    print(subtract(number_1, number_2))

else:
    print("Invalid input")
