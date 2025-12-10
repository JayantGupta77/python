class Solution(object):
    def countTriples(self, n):
        
        count = 0
        squares = set([i * i for i in range(1, n + 1)])
        
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a * a + b * b
                if c2 in squares:
                    c = int(c2 ** 0.5)
                    if c <= n:
                        count += 1
        return count
        