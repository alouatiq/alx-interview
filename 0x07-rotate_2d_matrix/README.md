# 0x07. Rotate 2D Matrix

## Description

This project focuses on implementing an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise using Python. The primary challenge is to manipulate the matrix directly without using extra space, demonstrating an understanding of in-place operations, matrix transposition, and row reversal.

## Requirements

* All code is written in Python 3 (version 3.8.10).
* No external libraries or modules are imported.
* Code must comply with `pycodestyle` (version 2.8.0).
* All Python scripts must be executable and start with `#!/usr/bin/python3`.
* A function `rotate_2d_matrix(matrix)` is implemented which performs the matrix rotation in-place.

## File Structure

* `0-rotate_2d_matrix.py`: Contains the implementation of the matrix rotation algorithm.
* `main_0.py`: Test file for validating the functionality of the rotation algorithm.

## Function Prototype

```python
def rotate_2d_matrix(matrix):
```

* `matrix`: a list of `n` lists, each containing `n` integers representing the 2D matrix.
* The function modifies the matrix in place and does not return anything.

## Example

Input:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_2d_matrix(matrix)
print(matrix)
```

Output:

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## How It Works

1. **Transpose the Matrix**: Convert rows to columns.
2. **Reverse Each Row**: After transposition, reverse each row to complete the rotation.

## Author

Project by ALX SE Program.
