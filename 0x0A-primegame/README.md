# 0x0A. Prime Game

## Description

Maria and Ben are playing a game involving prime numbers. In each round, a number `n` is given and players take turns choosing a prime number from a set of integers from `1` to `n`. Once chosen, that prime number and all of its multiples are removed from the set. The player unable to make a move loses the round. Maria always goes first.

This project implements an algorithm that determines the winner of the most rounds, assuming both players play optimally.

## File Structure

* `0-prime_game.py`: Contains the core logic for determining the game winner.
* `main_0.py`: (For testing) Sample script to execute the `isWinner` function with predefined inputs.

## Requirements

* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* The first line of all files must be:

  ```python
  #!/usr/bin/python3
  ```
* Code must follow the `PEP 8` style guide (version 1.7.x)
* All files must be executable
* No external libraries/modules are allowed

## Prototype

```python
def isWinner(x, nums):
    """x is the number of rounds,
    nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None"""
```

## Example

```python
x = 3
nums = [4, 5, 1]

# Round 1: Ben wins
# Round 2: Maria wins
# Round 3: Ben wins
# Result: Ben has the most wins

print(isWinner(x, nums))  # Output: 'Ben'
```

## Algorithm

1. Use the **Sieve of Eratosthenes** to efficiently compute prime numbers up to the largest `n`.
2. Count the number of prime numbers up to each `n`.
3. Use the parity of the count to decide who wins the round:

   * Odd count: Maria wins (starts first)
   * Even count: Ben wins
4. Compare scores over all rounds and return the winner.

## Author

* Hassan AL OUATIQ

## Repository

**GitHub repository:** [alx-interview](https://github.com/alouatiq/alx-interview)
**Directory:** `0x0A-primegame`
**File:** `0-prime_game.py`
