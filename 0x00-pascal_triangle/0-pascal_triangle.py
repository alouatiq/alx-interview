#!/usr/bin/python3
"""
0-pascal_triangle.py
Returns a list of lists of integers representing Pascal’s Triangle.
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing
    the Pascal’s triangle of n rows.
    If n <= 0, return an empty list.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # start with a row of 1’s
        row = [1] * (i + 1)
        # fill in the interior values
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    # this block only runs when executed directly, not when imported by the
    # auto‑checker
    from sys import argv

    try:
        n = int(argv[1]) if len(argv) > 1 else 5
    except ValueError:
        print("Usage: ./0-pascal_triangle.py <integer>")
        exit(1)

    tri = pascal_triangle(n)
    for row in tri:
        print("[{}]".format(",".join(str(x) for x in row)))
