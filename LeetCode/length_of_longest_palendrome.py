def longest_palindrome_length(s):
    n = len(s)
    if n == 0:
        return 0

    # dp[i][j] will be True if s[i:j+1] is a palindrome
    dp = [[False]*n for _ in range(n)]
    max_length = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length greater than 1
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if s[start] == s[end]:
                # If it's a 2 character or if the inner segment is palindrome
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    max_length = max(max_length, end - start + 1)
    return max_length

# Example usage:
s = "abcbab"
print(longest_palindrome_length(s))  # Output: 5
