def min_ones_integer_complexity(n, memo={}):
    if n == 1:
        return 1
    if n in memo:
        return memo[n]

    min_ones = n

    for i in range(1, n//2 + 1):
        min_ones = min(min_ones, min_ones_integer_complexity(i, memo) + min_ones_integer_complexity(n - i, memo))

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            min_ones = min(min_ones, min_ones_integer_complexity(i, memo) + min_ones_integer_complexity(n // i, memo))

    memo[n] = min_ones
    return min_ones

num = 12
print(f"Minimum number of ones to represent {num} (using + and *):", min_ones_integer_complexity(num))
