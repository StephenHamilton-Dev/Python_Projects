import random

'''
Author: Stephen Hamilton
Copyright: Copyright 2022, 
Usage: Player will enter in r, p, s and press enter. Upon pressing enter
       the game will tell the player what they chose and what the 
       computer chose. The game will also tell the player whether
       or not they have won based on those choices.
Description: Traditional Rock, Paper, Scissors game
Dev Repo: 
'''


def play_game():
    user_choice = input("Please input 'r' for rock, 's' for scissors, or 'p' for paper: ")
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        print(f"The computer chose {computer_choice} and you chose {user_choice}.\n")
        return 'It is a tie!'

    if player_wins(user_choice, computer_choice):
        print(f"The computer chose {computer_choice} and you chose {user_choice}.\n")
        return 'You Won!'
    else:
        print(f"The computer chose {computer_choice} and you chose {user_choice}.\n")
    return 'You Lost!'


def player_wins(player, opponent):
    if (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p') \
            or (player == 'r' and opponent == 's'):
        return True


print(play_game())
