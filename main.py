from game_functions import draw_board, player_turn, player_win

print("Welcome to Tic Tac Toe!\n"
      "\nTo quit the game, type the number 0 and press enter.\n")

# dictionary to create tictactoe board spaces
game_board_spaces = {1: "1", 2: "2", 3: "3",
                     4: "4", 5: "5", 6: "6",
                     7: "7", 8: "8", 9: "9"}

turn = 0
playing = True

while playing:

    # draw the first game board
    draw_board(game_board_spaces)

    print("\n")

    # ask the player for input
    player_input = input("To continue the game, please enter in a number for spaces 1 - 9 on the board and press"
                         " enter: ")

    # the player input, accessing a key in the dictionary, will be equal to each player turn
    game_board_spaces[int(player_input)] = player_turn(turn)

    # increment the turn by 1 every iteration of the loop
    turn += 1

    # if any combination of player win = true, end game and show the win, else, keep playing
    if player_win(game_board_spaces):
        print("You have won the game!")
        playing = False
    else:
        playing = True

    # if the player input is the number zero, end the game, else, keep playing the game
    if player_input == '0':
        print("The game has ended.")
        playing = False

# draw the final game board for the win
draw_board(game_board_spaces)
