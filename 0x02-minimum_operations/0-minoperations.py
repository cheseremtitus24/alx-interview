#!/usr/bin/python3
"""Finds minimum number of operations needed to print H's

This file can also be imported as a module and contains
the following functions:
    * minOperations- is a function that finds least amount of operations to copy
        and paste H's a set n-number of times

"""


def minOperations(n):
    """Finds the least number of operations needed to get specified number of H's

    Parameters
    ----------
    n :  int
        The number of H's to generate

    Returns
    -------
    int:
        number of operations
    """
    operations = 0
    idx = 2
    if n < 2:
        return 0
    while (idx < n + 1):
        while n % idx == 0:
            operations += idx
            n /= idx
        idx += 1
    return operations
