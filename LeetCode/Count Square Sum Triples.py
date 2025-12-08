class Solution(object):
    def countTriples(self, n):
        
        count = 0
        # Precompute squares for efficiency
        squares = set([i * i for i in range(1, n + 1)])
        
        # Iterate through possible values of a and b
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a * a + b * b
                # Check if c^2 is a perfect square within range
                if c2 in squares:
                    c = int(c2 ** 0.5)
                    if c <= n:
                        count += 1
        return count
        