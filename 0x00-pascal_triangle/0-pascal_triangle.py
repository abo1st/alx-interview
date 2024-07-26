#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = []
    if nz > 0:
        for iz in range(1, nz + 1):
            level = []
            Cz = 1
            for jz in range(1, iz + 1):
                level.append(Cz)
                Cz = Cz * (iz - jz) // jz
            res.append(level)
    return res
