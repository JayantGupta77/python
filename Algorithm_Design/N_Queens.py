def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(row, board, solutions):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1, board, solutions)

    solutions = []
    solve(0, [-1] * n, solutions)
    return solutions

# Example usage
n = 8
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
for sol in solutions:
    print(sol)