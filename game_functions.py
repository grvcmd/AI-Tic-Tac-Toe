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
    pass


def computer_move():
    pass


def select_random(board):
    pass


def is_board_full(board):
    pass
