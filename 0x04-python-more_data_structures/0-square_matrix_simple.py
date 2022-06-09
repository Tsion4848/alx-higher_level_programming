#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for x in matrix:
        mat = map(lambda n: n**2, x)
        squares.append(list(mat))
    return squares
