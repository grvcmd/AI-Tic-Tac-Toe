"""This file will hold all functions used when playing a game of Tic Tac Toe in main.py"""

board = [' ' for x in range(10)]


def insert_letter(letter, position):
    board[position] = letter


def space_is_free(position):
    return board[position] == " "


def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def is_winner(board, letter):
    return (board[7] == letter and board[8] == letter and board[9] == letter) or \
           (board[4] == letter and board[5] == letter and board[6] == letter) or \
           (board[1] == letter and board[2] == letter and board[3] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[3] == letter and board[6] == letter and board[9] == letter)


def player_move():
    run = True
    while run:
        move = input("Select a position to place an 'X' (1-9)")
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print("Please choose a number within the range!")
        except:
            print("Please choose a number!")


def computer_move():
    pass


def select_random(board):
    pass


def is_board_full(board):
    if board.count(' ') > 1:
        return True
    else:
        return False
