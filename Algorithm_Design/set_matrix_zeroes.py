def set_matrix_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    row_zero = set()
    col_zero = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in row_zero or j in col_zero:
                matrix[i][j] = 0

    return matrix

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

result = set_matrix_zeros(matrix)
print(result)
