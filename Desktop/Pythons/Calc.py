def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    return x / y
def exponential(x, y):
    return x ** y

x = float(input("First number: "))
y = float(input("Second number: "))
userChoice = input("What would you like to do (addtion, subtraction, multiplication, division or exponential)? ")

if userChoice == "addition":
    print(addition(x, y))
elif userChoice == "subtraction":
    print(subtraction(x, y))
elif userChoice == "multiplication":
    print(multiplication(x, y))
elif userChoice == "division":
    print(division(x, y))
elif userChoice == "exponential":
    print(exponential(x, y))
else:
    print("invalid order")




