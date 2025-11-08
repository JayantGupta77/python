def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    i, j = m, n
    lcs_seq = []
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_seq.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs_seq))

str1 = "AGGTAB"
str2 = "GXTXAYB"
length, sequence = lcs(str1, str2)
print("Length of LCS:", length)       
print("LCS:", sequence)                 
