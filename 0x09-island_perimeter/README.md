# 0x09. Island Perimeter

## Description

This project is part of the ALX Interview Preparation series and focuses on calculating the perimeter of an island in a grid. The island is represented by `1`s (land) and is surrounded by `0`s (water). The objective is to determine the total perimeter of the landmass using basic algorithmic logic in Python.

## Learning Objectives

* Understand how to traverse and analyze 2D arrays (matrices)
* Use conditional logic to calculate geometric properties
* Apply counting techniques for algorithm design

## Requirements

* Allowed editors: `vi`, `vim`, `emacs`
* Files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* Code must follow PEP 8 style (version 1.7)
* No imports allowed
* All functions must be documented
* All files must be executable

## File Descriptions

### 0-island\_perimeter.py

Contains the function `island_perimeter(grid)` which calculates and returns the perimeter of the island described in a 2D grid.

### 0-main.py

Provides a test case to run and verify the perimeter calculation using a sample grid.

## Usage

To test the function, run:

```bash
$ ./0-main.py
```

Expected output for the provided example:

```
12
```

## Example

```python
# grid sample in 0-main.py
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Author

* ALX SE Program
