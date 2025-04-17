#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    If n is less than or equal to 0, returns an empty list.
    """
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Loop to generate each row from row index 1 to n-1
    for i in range(1, n):
        prev_row = triangle[-1]
        # Start each row with a 1
        row = [1]
        # Loop through positions in the previous row to compute the middle values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        # End each row with a 1
        row.append(1)
        triangle.append(row)
    
    return triangle


# The following main block is for testing purposes.
if __name__ == "__main__":
    # Example tests: Feel free to modify the value to check different cases.
    tests = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for test in tests:
        print("Pascal's Triangle with", test, "rows:")
        for row in pascal_triangle(test):
            print(row)
        print("-" * 30)
