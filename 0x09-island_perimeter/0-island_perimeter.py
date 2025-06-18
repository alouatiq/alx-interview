#!/usr/bin/python3
"""
0-island_perimeter
This module contains a function that calculates the perimeter of an island
represented in a 2D grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Parameters:
    grid (list of list of int): 2D grid where 0
    represents water and 1 represents land

    Returns:
    int: the perimeter of the island
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check the cell above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                # Check the cell to the left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
