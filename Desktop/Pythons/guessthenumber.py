import random

number_to_guess = random.randint(1, 101)
user_guess = int(input("Guess a number between 1 and 100: "))
if user_guess < number_to_guess:
    print("To low")
elif user_guess > number_to_guess:
    print("To high")
else:
    print("Perfect")
    