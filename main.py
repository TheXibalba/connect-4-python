import numpy as np
from tabulate import tabulate
# Input rows and columns
while(True):
    try:
        r = int(input("Rows: "))
        c = int(input("Columns: "))
    except ValueError:
        print("Invalid Input!")
    else:
        break

# Input pieces
while(True):
    p = int(input("Pieces: "))
    if(p <= 0):
        (print(
            f"You cannot have {p} pieces to connect. \nPlease enter a positive, non-zero integer for the number of pieces to connect: "))
    else:
        break

# Create a zero-filled array of size r*c
board = np.zeros((r, c), dtype=int)
allowed_moves = [r]*c


# Display the board
def show_board():
    # print(np.where(board == -1, 2, board))
    print(tabulate(board, tablefmt="fancy_grid"))


# Check if the column and row are valid
def check_it(row, col):
    for i in range(0 if row <= (p-1) else row-(p-1), (p-1) if row >= 2 else row+1):
        for j in range(0 if col <= (p-1) else col-(p-1), p if col >= (p-1) else col+1):
            current_board = board[i:i+p, j:j+p]
            for k in range(p):
                if sum(current_board[k]) == TURN*p or sum(current_board[:, k]) == TURN*p:
                    return True
            if sum(np.diag(current_board)) == TURN*p or sum(np.diag(current_board[::-1])) == TURN*p:
                return True

# Find the row


def find_row(col):
    return (r-1)-np.where(board[::-1, col] == 0)[0][0]

# Player turn function


def player_turn():
    return 1 if TURN == 1 else 2

# Take in the column number as an input and return 1 for player 1 and 2 for player 2


def ip_move():
    while True:
        try:
            move = int(
                input(f"Player {player_turn() }, what column do you want to put your piece? "))-1
            if move in range(c) and allowed_moves[move] != 0:
                allowed_moves[move] -= 1
                return move
            continue
        except ValueError:
            continue


TURN = 1
show_board()
while True:
    move = ip_move()
    row = find_row(move)
    board[row, move] = TURN
    show_board()
    if check_it(row, move):
        print(f"Player {player_turn()} has won!")
        break
    if sum(allowed_moves) == 0:
        print("TIE!")
        break
    TURN *= -1
