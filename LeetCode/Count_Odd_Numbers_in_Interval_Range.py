class Solution(object):
    def countOdds(self, low, high): 
        return ((high - low) // 2) + (1 if (low % 2 == 1 or high % 2 == 1) else 0)