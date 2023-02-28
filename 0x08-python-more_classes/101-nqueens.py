#!/usr/bin/python3

import sys

def nqueens(N):
    # Initialize empty board with 0's
    board = [[0 for x in range(N)] for y in range(N)]
    solutions = []
    # Recursive helper function
    def solve(board, col):
        # Base case: if all queens are placed, add solution
        if col == N:
            queens = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        queens.append((i, j))
            solutions.append(queens)
            return True
        # Check each row in the current column
        for i in range(N):
            # Check if queen can be placed in this row
            if is_safe(board, i, col):
                # Place queen
                board[i][col] = 1
                # Recursive call on next column
                solve(board, col+1)
                # Backtrack
                board[i][col] = 0
        # If no queen can be placed in this column, return False
        return False

    # Check if a queen can be placed at board[row][col]
    def is_safe(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        # Check lower diagonal on left side
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        # Queen can be placed
        return True

    # Call recursive function on first column
    solve(board, 0)

    # Print solutions in desired format
    for queens in solutions:
        solution = []
        for i in range(N):
            row = []
            for j in range(N):
                if (i, j) in queens:
                    row.append(1)
                else:
                    row.append(0)
            solution.append(row)
        print(solution)

# Check if program was called with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Try to parse argument as integer
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Call nqueens function with N
nqueens(N)
