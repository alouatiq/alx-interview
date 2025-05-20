#!/usr/bin/python3
"""
N Queens solver module
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard.
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed at board[row][col]
    
    Args:
        board: list of lists representing the chessboard
        row: row to check
        col: column to check
        n: size of the board
        
    Returns:
        Boolean: True if placing a queen at board[row][col] is safe
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Recursive utility function to solve N Queens problem
    
    Args:
        board: list of lists representing the chessboard
        col: current column being processed
        n: size of the board
        solutions: list to store the solutions
        
    Returns:
        Boolean: True if a solution exists, False otherwise
    """
    # Base case: If all queens are placed, add the solution
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    # Consider this column and try placing the queen in all rows
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen
            board[i][col] = 1

            # Recur to place rest of the queens
            res = solve_nqueens_util(board, col + 1, n, solutions) or res

            # Backtrack
            board[i][col] = 0

    return res


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all solutions
    
    Args:
        n: size of the board
    """
    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    # Solve the N Queens problem
    solve_nqueens_util(board, 0, n, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


def main():
    """
    Main function to parse arguments and call the solver
    """
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a valid integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(n)


if __name__ == "__main__":
    main()
