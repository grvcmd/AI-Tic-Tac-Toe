from game_functions import *


if __name__ == '__main__':
    print("Welcome to Tic Tac Toe!")
    print_board()

    while not is_board_full(board):
        # Check if computer has a winning line
        if not(is_winner(board, 'O')):
            player_move()
            print_board()
        else:
            print("Sorry, O's won this time!")
            break

        # Check if player has a winning line
        if not(is_winner(board, 'X')):
            computer_move()
            print_board()
        else:
            print("X's won this time! Good Job!")

    if is_board_full(board):
        print('Tie Game!')


