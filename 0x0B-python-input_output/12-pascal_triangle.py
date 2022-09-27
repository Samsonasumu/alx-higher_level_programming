#!/usr/bin/python3

"""Modules that returns a list of lists of integers representing
the Pascal's triangle of ``n``.
"""


def pascal_triangle(n):
    """Function that returns the Pascal triangle n.

    Args:
        n: size of the triangle (rows)

    Returns:
        matrix: a matrix with the pascal triangle

    """
    if n <= 0:
        return []

    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
