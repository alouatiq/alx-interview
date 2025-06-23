#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

if __name__ == "__main__":
    x = 5
    nums = [2, 5, 1, 4, 3]
    print("Winner: {}".format(isWinner(x, nums)))
