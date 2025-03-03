def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def flatten_matrix(matrix):
    return [item for sublist in matrix for item in sublist]