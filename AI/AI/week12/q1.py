# Taking the number of queens as input from the user
print("Enter the number of queens:")
N = int(input())

# Create an NxN chessboard (matrix) with all elements set to 0
board = [[0] * N for _ in range(N)]

def attack(i, j):
    # Check vertically and horizontally
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # Check diagonally
    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def N_queens(n):
    if n == 0:
        return True
    for i in range(N):
        for j in range(N):
            if (not attack(i, j)) and (board[i][j] != 1):
                board[i][j] = 1
                if N_queens(n - 1) == True:
                    return True
                board[i][j] = 0
    return False

# Solve the problem
N_queens(N)

# Print the board
for row in board:
    print(row)
