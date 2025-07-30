import random

number_to_guess = random.randint(1, 100)
found = False

while not found:
    user_guess = input("whats my number: ")

    if int(user_guess) < number_to_guess:
        print("to low")
    elif int(user_guess) > number_to_guess:
        print("to high")
    else: 
        found = True
        print("HIT")



    




