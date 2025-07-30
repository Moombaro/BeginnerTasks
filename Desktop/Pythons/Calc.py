import math




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
def dividible(x, y):
    return y % x
def root(x):
    return math.sqrt(x)
def root(y):
    return math.sqrt(y)


x = float(input("First number: "))
y = float(input("Second number: "))
userChoice = input("What would you like to do (addtion, subtraction, multiplication, division, exponential, root or dividible)? ")

if userChoice == "addition":
    print(x, "+", y, "=", addition(x, y))
elif userChoice == "subtraction":
    print(x, "-", y, "=", subtraction(x, y))
elif userChoice == "multiplication":
    print(x, "*", y, "=", multiplication(x, y))
elif userChoice == "division":
    print(x, "/", y, "=", division(x, y))
elif userChoice == "exponential":
    print(x, "^", y, "=", exponential(x, y))
elif userChoice == "dividible":
    print(dividible(x, y))
elif userChoice == "root":
    print("Root of ", x, "=", root(x))
    print("Root of ", y, "=", root(y))
else:
    print("invalid order")




