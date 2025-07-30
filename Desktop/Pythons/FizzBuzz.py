print("Object is to create a List 1 - 100, and replace multiples of 3 by 'Fizz', multiples of 5 by 'Buzz' and if they collide 'FizzBuzz'.")


x = 1
for myList in range(1, 101):
    if myList % 15 == 0:
        print("FizzBuzz")
    elif myList % 5 == 0:
        print("Buzz")
    elif myList % 3 == 0:
        print("Fizz")
    else:
        print(myList)
