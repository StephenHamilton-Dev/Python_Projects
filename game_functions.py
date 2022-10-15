# function to draw game board and fill each space on the board with the space number
def draw_board(game_board_spaces):
    game_board = (f"|{game_board_spaces[1]}|{game_board_spaces[2]}|{game_board_spaces[3]}|\n"
                  f"|{game_board_spaces[4]}|{game_board_spaces[5]}|{game_board_spaces[6]}|\n"
                  f"|{game_board_spaces[7]}|{game_board_spaces[8]}|{game_board_spaces[9]}|")
    print(game_board)


# function to switch player turn
def player_turn(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'


# function to decide if player wins
def player_win(game_board_spaces):
    if (game_board_spaces[1] == game_board_spaces[2] == game_board_spaces[3]) or \
       (game_board_spaces[4] == game_board_spaces[5] == game_board_spaces[6]) or \
       (game_board_spaces[7] == game_board_spaces[8] == game_board_spaces[9]):
        return True
    elif (game_board_spaces[1] == game_board_spaces[4] == game_board_spaces[7]) or \
         (game_board_spaces[2] == game_board_spaces[5] == game_board_spaces[8]) or \
         (game_board_spaces[3] == game_board_spaces[6] == game_board_spaces[9]):
        return True
    elif (game_board_spaces[1] == game_board_spaces[5] == game_board_spaces[9]) or \
         (game_board_spaces[3] == game_board_spaces[5] == game_board_spaces[7]):
        return True
    else:
        return False

