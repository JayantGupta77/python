def set_matrix_zeroes(matrix):
    if not matrix or not matrix[0]:
        return
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Check if first row or column contains zero
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
    
    # Mark zeros in first row and column and all lines
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Set matrix elements to zero based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Zero out first row if originally contained zero
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    # Zero out first column if originally contained zero
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0
