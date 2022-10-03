import os
import random


computer_wins = 0
user_wins = 0

print("Welcome to Rock, Paper, Scissors!\n")

print("This game will be won after winning 3 rounds. Ties do not count.\n")

# create logical control structures for game to decide is user wins or computer wins (if, elif, else, etc...)
while user_wins < 3 and computer_wins < 3:

    computer_choice = random.choice(['r', 'p', 's'])
    user_choice = input("Please input a 'r' for Rock, 'p', for Paper, or 's' for Scissors: \n")

    if user_choice == 'r' and computer_choice == 's':
        user_wins = user_wins + 1
        print(f"You chose {user_choice} and the computer {computer_choice}, you won this round!\n")
    elif user_choice == 's' and computer_choice == 'p':
        user_wins = user_wins + 1
        print(f"You chose {user_choice} and the computer {computer_choice}, you won this round!\n")
    elif user_choice == 'p' and computer_choice == 'r':
        user_wins = user_wins + 1
        print(f"You chose {user_choice} and the computer {computer_choice}, you won this round!\n")
    elif user_choice == computer_choice:
        print(f"You chose {user_choice} and the computer chose {computer_choice}.\n")
        print("It is a tie! No winner for this round!\n")
    else:
        computer_wins = computer_wins + 1
        print(f"You chose {user_choice} and the computer {computer_choice}, the computer won this round!\n")


if user_wins == 3:
    print("You have won 3 rounds!. You won the game!\n")
elif computer_wins == 3:
    print("The computer has won 3 rounds!. You lost the game!\n")

os.system('PAUSE')

exit(0)





