#!/usr/bin/python3
"""
This program rotates 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """This rotates two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for iz in range(int(n / 2)):
        y = (n - iz - 1)
        for j in range(iz, y):
            x = (n - 1 - j)
            # current number
            tmp = matrix[iz][j]
            # change top for left
            matrix[iz][j] = matrix[x][iz]
            # change left for bottom
            matrix[x][iz] = matrix[y][x]
            # change bottom for right
            matrix[y][x] = matrix[j][y]
            # change right for top
            matrix[j][y] = tmp
