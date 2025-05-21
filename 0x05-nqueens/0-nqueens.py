#!/usr/bin/python3
"""Solve the N queens problem.

The program prints every possible way to place N queens on an N×N
chessboard so that no two queens attack each other, one solution per line.

Usage:
    $ ./0-nqueens.py N

N must be an integer ≥ 4.
"""

import sys


def is_safe(queens, col):
    """Return True if placing a queen at (current_row, col) is safe."""
    row = len(queens)
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, queens=None):
    """Recursively place queens and print each valid configuration."""
    if queens is None:
        queens = []

    row = len(queens)
    if row == n:
        print([[r, c] for r, c in enumerate(queens)])
        return

    for col in range(n):
        if is_safe(queens, col):
            queens.append(col)
            solve_nqueens(n, queens)
            queens.pop()


def main():
    """Validate arguments and start solving."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == '__main__':
    main()
