__author__ = 'Bruno'

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(7):

    print("Turn", turn + 1)

    guess_row = int(input("Guess Row:")) - 1
    guess_col = int(input("Guess Col:")) - 1
    error = False

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break

    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
            error = True
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")

    if not error:
        board[guess_row][guess_col] = "X"

    print_board(board)
    print()
    if turn == 6:
        print("Game Over")
