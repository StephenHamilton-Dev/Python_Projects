import random
import os

'''
Author: Stephen Hamilton
Copyright: Copyright 2022, Computer - Random Number Guessing Game
Usage: Simple beginner level random number guessing game
       used for exercising python programming basics
Description: When this program is run, the user is to select
             a random number in between 1 and 10 for the computer
             to guess. From there, the user inputs c, h, or l, and
             if the computer guessed the users number correctly, 
             the user types in c.
Dev Repo: https://github.com/StephenHamilton-Dev/Python_Projects/new/Computer_Num_Guess_Game
'''

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    print("In this game, the computer is going to guess a number between 1 and 10.\n"
          "The user will be prompted with a guess the computer made.\nOnce prompted,"
          "the user will then enter (c) for correct, (h) for too high, and (l) for too"
          " low.\n")
    print("Come up with a number in between 1 and 10 for the computer to guess, then press enter to start the game.\n")
       
    os.system("pause")

    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)?\n")
        if feedback == 'h':
            high = guess - 1
            print("Guess was too high\n")
        elif feedback == 'l':
            low = guess + 1
            print("Guess was too low\n")
        elif feedback == 'c':
            print("The computer guessed your number!\n")


computer_guess(10)
