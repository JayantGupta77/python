def upside_down_matrix(matrix):
    return matrix[::-1]

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = upside_down_matrix(mat)
for row in result:
    print(row)
