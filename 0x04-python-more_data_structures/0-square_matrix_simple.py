def square_matrix_simple(matrix=[]):
    squares = []
    for x in range(0, len(matrix)):
        squares[x] = matrix[x] ** 2
    return squares
