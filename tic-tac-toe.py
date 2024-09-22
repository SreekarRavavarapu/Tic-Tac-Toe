#Author: Sreekar Ravavarapu
#Email: sravavarapu@umass.edu
#Spire ID: 34515445

def print_board(n, board):
  # premake +---+ style boundary using string mutiplication and concatination
  boundary_line = ("+---" * n) + "+"
  # range over every row in board (an n by n board)
  for i in range(n):
    # print a leading boundary line
    print(boundary_line)
    # start string for row i with leading bar
    row_i = "|"
    # range over every column in board (an n by n board)
    for j in range(n):
      # update row_i string with space, characher from board, space, and trailing bar
      # this completes "cell j" for row i
      row_i += " " + board[i][j] + " " + "|"
    # print the completed row i
    print(row_i)
  # print final boundary line
  print(boundary_line)
def make_empty_board(n):
    # Create an empty tic-tac-toe board
    return [[' ' for _ in range(n)] for _ in range(n)]

def get_location(n, board):
    while True:
        row_input = input(f"Please enter a row index between 0 and {n-1}: ")
        col_input = input(f"Please enter a column index between 0 and {n-1}: ")

        if not (row_input.isdigit() and col_input.isdigit()):
            print(f"({row_input}, {col_input}) is not a legal input!")
            continue

        r, c = int(row_input), int(col_input)
        if r < 0 or r >= n or c < 0 or c >= n:
            print(f"({r}, {c}) is not a legal space!")
            continue

        if board[r][c] != ' ':
            print(f"({r}, {c}) is not an available space!")
            continue

        return r, c

def has_won(n, board, player):
    # Check rows and columns for a win
    for i in range(n):
        if all(board[i][x] == player for x in range(n)):
            return True
        if all(board[x][i] == player for x in range(n)):
            return True

    # Check diagonals for a win
    if all(board[i][i] == player for i in range(n)):
        return True
    if all(board[i][n-1-i] == player for i in range(n)):
        return True

    return False

def play_game(n):
    board = make_empty_board(n)
    print(f"*** Welcome to {n} by {n} Tic-Tac-Toe ***")
    print_board(n, board)

    current_player = 'X'
    moves = 0
    max = n * n

    while moves < max:
        print(f"* {current_player}'s turn *")
        r, c = get_location(n, board)
        board[r][c] = current_player
        print_board(n, board)

        if has_won(n, board, current_player):
            print(f"{current_player} wins!")
            break

        current_player = 'O' if current_player == 'X' else 'X'
        moves += 1

    if moves == max:
        print("Tie!")

play_game(3)  
