number1 = input("First Number: ")
number2 = input("Second Number: ")
add = (int(number1) + int(number2))
sub = (int(number1) - int(number2))
mult = (int(number1) * int(number2))
div = (int(number1) / int(number2))
end = False
def Calculator():
    
    userReply = input("What would you like to do? (add, sub, mult, div): ")

    if userReply == "add":
        print("The result is: {}".format(add))
    elif userReply == "sub":
        print("The result is: {}".format(sub))
    elif userReply == "mult":
        print("The result is: {}".format(mult))
    else:
        userReply == "div"
        print("The result is: {}".format(div))
        
        
def Repeat():
        while True:
            userReply = input("Are you done? (yes/no): ")
    
            if userReply == "yes":
                print("Have a nice day")
                break
            else:
                return Calculator()

Calculator()
Repeat()


     
        