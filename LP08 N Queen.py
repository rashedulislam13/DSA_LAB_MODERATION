import copy
import random
def take_input():
    # Accepts the size of the chess board
    while True:
        try:
            n = int(input('Input size of queen? n = '))
            if n <= 3:
                print("Enter a value greater than or equal to 4")
                continue
            return n
        except ValueError:
            print("Invalid value entered. Enter again")


def get_board(n):
    # Returns an n by n board
    board = ["."] * n
    for i in range(n):
        board[i] = ["."] * n
    return board


def print_solution(solutions, n):
    # Prints one of the solutions randomly
    x = random.randint(0, len(solutions) - 1)  # 0 and len(solutions)-1 are inclusive
    for row in solutions[x]:
        print(" ".join(row))


def solve(board, col, n):
    # Use backtracking to find all solutions
    if col >= n:
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            if col == n - 1:
                add_solution(board)
                board[i][col] = "."
                return
            solve(board, col + 1, n)  # recursive call
            # backtrack
            board[i][col] = "."


def is_safe(board, row, col, n):
    # Check if it's safe to place a queen at board[x][y]
    # check row on left side
    for j in range(col):
        if board[row][j] == "Q":
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i = i - 1
        j = j - 1

    x, y = row, col
    while x < n and y >= 0:
        if board[x][y] == "Q":
            return False
        x = x + 1
        y = y - 1

    return True


def add_solution(board):
    # Saves the board state to the global variable: solutions
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


# Taking size of the chessboard from user
n = take_input()

# Returns a square board of nxn dimension
board = get_board(n)

# Empty list of all possible solutions
solutions = []

# Solving using backtracking
solve(board, 0, n)

print()

print("One of the solutions is: \n")
print_solution(solutions, n)

print()
print("Total number of solutions=", len(solutions))
