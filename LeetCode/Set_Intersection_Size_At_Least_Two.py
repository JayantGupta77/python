class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        a = -1
        b = -1
        ans = 0
        
        for s, e in intervals:
            if s > b:
                ans += 2
                b = e
                a = e - 1
            elif s > a:
                ans += 1
                a = b
                b = e
        
        return ans
