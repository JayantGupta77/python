class Solution(object):
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        prev = [[0] * k for _ in range(n)]

        for i in range(m):
            cur = [[0] * k for _ in range(n)]
            for j in range(n):
                val_mod = grid[i][j] % k

                if i == 0 and j == 0:
                    cur[0][val_mod] = 1
                    continue

                if i > 0:
                    for r in range(k):
                        cnt = prev[j][r]
                        if cnt:
                            cur[j][(r + val_mod) % k] = (cur[j][(r + val_mod) % k] + cnt) % MOD

                if j > 0:
                    for r in range(k):
                        cnt = cur[j-1][r]
                        if cnt:
                            cur[j][(r + val_mod) % k] = (cur[j][(r + val_mod) % k] + cnt) % MOD

            prev = cur 

        return prev[n-1][0]