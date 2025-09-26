def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

product = multiply_matrices(A, B)
for row in product:
    print(row)