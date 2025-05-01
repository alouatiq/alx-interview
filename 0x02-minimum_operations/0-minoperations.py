#!/usr/bin/python3
"""Module for minimum operations problem."""


def minOperations(n):
    """Compute the minimum operations to produce n H characters.

    Args:
        n (int): Target number of H characters.

    Returns:
        int: Fewest number of operations or 0 if impossible.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
