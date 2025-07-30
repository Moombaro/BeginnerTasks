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
    return x % y
def root(x):
    return math.sqrt(x)
def root(y):
    return math.sqrt(y)

def Calculator():
    while True:
        try:
            print("This is a test calculator!")
            print("Pleas choose your function:")
            print("1. addition")
            print("2. subtraction")
            print("3. multiplication")
            print("4. division")
            print("5. exponential")
            print("6. dividible /even<>odd")
            print("7. root")
            userChoice = input("choose your number: ")
            x = float(input("First number: "))
            y = float(input("Second number: "))

         
        
            

            if userChoice == "1":
                print(x, "+", y, "=", addition(x, y))
            elif userChoice == "2":
                print(x, "-", y, "=", subtraction(x, y))
            elif userChoice == "3":
                print(x, "*", y, "=", multiplication(x, y))
            elif userChoice == "4":
                print(x, "/", y, "=", division(x, y))
            elif userChoice == "5":
                print(x, "^", y, "=", exponential(x, y))
            elif userChoice == "6":
                if dividible(x, y) == 0:
                    print(x, "is clearly dividible by ", y)
                else:
                    print(x, "is not clearly dividible by ", y)
            elif userChoice == "7":
                print("Root of ", x, "=", root(x))
                print("Root of ", y, "=", root(y))
            else:
                print("invalid order")
        except ValueError and ZeroDivisionError:
            return print("invalid input")
        
        keep_going = input("do you want to continue? (yes/no) ")
        if keep_going == "no":
            print("Have a nice day!")
            break 
        




Calculator()





