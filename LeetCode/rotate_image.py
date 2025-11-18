def rotate_image(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()

image = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_image(image)

for row in image:
    print(row)