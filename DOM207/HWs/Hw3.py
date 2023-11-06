# 6) Guessing game

import random

# Welcome message
print("Welcome to the guessing game")

# Generating the random number
number = random.randint(1, 20)

# Getting the guess
for i in range(4):
    guess = input("Enter your guess: ")
    try:
        guess = int(guess)  # Try converting to an integer
    except ValueError:
        try:
            guess = float(guess)  # Try converting to a float
            guess = int(guess)  # Convert to an integer
        except ValueError:
            print("Please enter a valid number.")
            continue
    if guess == number:
        print("Congratulations, you've won the game!")
        print("You took {} attempts to guess the number.".format(i + 1))
        break
    elif guess < number:
        print("Your guess is lower than the number.")
    else:
        print("Your guess is higher than the number.")
else:
    print("You've lost the game.")
    print("The number was {}.".format(number))

