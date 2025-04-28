#!/usr/bin/python3
"""Module for minimum operations problem."""


def minOperations(n):
    """Calculate the fewest number of operations needed to get n H characters.
    
    Args:
        n (int): The number of H characters desired.
        
    Returns:
        int: Minimum number of operations needed, or 0 if impossible.
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
