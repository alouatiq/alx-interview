# 0x02. Minimum Operations

## Description

This project focuses on calculating the minimum number of operations needed to generate exactly `n` characters `H` in a text file, using only two allowed operations:
- **Copy All**: Copies the entire content.
- **Paste**: Pastes the copied content.

The goal is to find the fewest number of operations required to achieve `n` characters.

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should follow PEP 8 style (version 1.7.x)
- All files must be executable
- Must include a `README.md` file

---

## Approach

To solve the problem efficiently:
- We use **Prime Factorization**.
- For each prime factor of `n`, we add the factor to the number of operations.
- The idea is that building `n` characters is most efficient when we repeatedly copy and paste groups of characters, and the cost is minimized by splitting `n` into its prime components.

For example:
- `n = 9`
  - Prime factors are [3, 3]
  - Minimum operations = 3 + 3 = 6

- `n = 12`
  - Prime factors are [2, 2, 3]
  - Minimum operations = 2 + 2 + 3 = 7

If `n` is less than or equal to 1, the answer is `0` since no operations are needed.

---

## Usage

### Example

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""Main file for testing"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```
