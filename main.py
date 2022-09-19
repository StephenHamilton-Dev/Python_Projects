import random

'''
Author: Stephen Hamilton
Copyright: Copyright 2022, Random Number Guessing Game
Usage: Simple beginner level random number guessing game
       used for exercising python programming basics
Dev Repo: https://github.com/MyGITRepo-dev/Python_Projects
'''


# initialize a variable to hold the value of a random number in range 1 to 10
random_num = random.randint(1, 10)

# initialize a variable to hold value of guess
guess = 0

# Let user know that the random number guess game has started
print("Welcome To The Random Number Guessing Game! Let's Get Started!\n")

# run through while loop until user guesses correct number
while guess != random_num:
    # ask user to input guess
    guess = int(input("Please enter in a number from 1 to 10: "))
    if guess > 10:
        print("\nSorry, the number you guessed is too high.\n")
    elif guess < 1:
        print("\nSorry, the number you guessed is too low.\n")
    elif guess != random_num:
        print("\nSorry, wrong number, please guess again.\n")
    elif guess == random_num:
        print("\nCongratulations! You guessed the correct number!\n")
