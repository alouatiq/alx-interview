#!/usr/bin/python3
"""
Prime Game - determine the winner after x rounds
"""


def sieve_of_eratosthenes(n):
    """Return a list of prime counts up to n using sieve."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    primes_count = [0] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if sieve[i]:
            count += 1
        primes_count[i] = count
    return primes_count


def isWinner(x, nums):
    """Determine who is the winner of most rounds.

    Args:
        x (int): number of rounds
        nums (list): list of n for each round

    Returns:
        str: name of the player with most wins, or None
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes_up_to = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_up_to[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
