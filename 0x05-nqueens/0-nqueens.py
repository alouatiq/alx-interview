#!/usr/bin/python3
import sys


def is_safe(queen, queens):
    """Check if the queen placement is safe from attacks."""
    for row, col in enumerate(queens):
        if col == queen or \
           col - row == queen - len(queens) or \
           col + row == queen + len(queens):
            return False
    return True


def solve_nqueens(n):
    """Solve the N queens problem using backtracking."""
    def backtrack(queens):
        row = len(queens)
        if row == n:
            solutions.append([[r, c] for r, c in enumerate(queens)])
            return
        for col in range(n):
            if is_safe(col, queens):
                queens.append(col)
                backtrack(queens)
                queens.pop()

    solutions = []
    backtrack([])
    return solutions


def main():
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

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
