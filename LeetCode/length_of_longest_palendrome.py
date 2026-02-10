def longest_palindrome_length(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [[False]*n for _ in range(n)]
    max_length = 1

    for i in range(n):
        dp[i][i] = True

    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if s[start] == s[end]:
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    max_length = max(max_length, end - start + 1)
    return max_length

# Example usage:
s = "abcbab"
print(longest_palindrome_length(s)) 
