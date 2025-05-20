#!/usr/bin/python3
"""
N Queens solver
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard.
"""
import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed at position [row, col]
    
    Args:
        board: list of queen positions [row, col]
        row: row to check
        col: column to check
        
    Returns:
        Boolean: True if position is safe
    """
    for r, c in board:
        # Check if same row, same column, or same diagonal
        if r == row or c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, row=0, board=None, solutions=None):
    """
    Solve the N Queens problem using backtracking
    
    Args:
        n: size of the board
        row: current row being processed
        board: list of queen positions [row, col]
        solutions: list to store all solutions
    """
    if board is None:
        board = []
    if solutions is None:
        solutions = []

    # Base case: If all queens are placed
    if row == n:
        solutions.append(board.copy())
        return solutions

    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col):
            # Place the queen
            board.append([row, col])
            
            # Recur to place rest of the queens
            solve_nqueens(n, row + 1, board, solutions)
            
            # Backtrack
            board.pop()
    
    return solutions


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
    solutions = solve_nqueens(n)
    
    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
