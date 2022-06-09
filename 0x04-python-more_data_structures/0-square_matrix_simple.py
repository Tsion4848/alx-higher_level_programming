#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    squares = [x**2 for x in range(0, len(matrix))]
    return squares
