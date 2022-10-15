from game_functions import draw_board, player_turn, player_win

# dictionary to create tictactoe board spaces
game_board_spaces = {1 : "1", 2 : "2", 3 : "3",
                     4 : "4", 5 : "5", 6 : "6",
                     7 : "7", 8 : "8", 9 : "9"}

print("Welcome to Tic Tac Toe!\n"
      "To quit the game, type the word quit and press enter.\n")

turn = 0
playing = True

while playing:

    # ask the player for input
    player_input = input("Please enter in a number for spaces 1 - 9: ")

    # the player input, accessing a key in the dictionary, will be equal to each player turn
    game_board_spaces[int(player_input)] = player_turn(turn)

    # draw the first game board
    draw_board(game_board_spaces)

    # increment the turn by 1 every iteration of the loop
    turn += 1

    # if any combination of player win = true, end game and show the win, else, keep playing
    if player_win(game_board_spaces):
        print("You have won the game")
        playing = False
    else:
        playing = True

    # if the player input is the word quit, end the game, else, keep playing the game
    if player_input == 'quit':
        print("The game has ended")
        playing = False

# draw the final game board for the win
draw_board(game_board_spaces)


