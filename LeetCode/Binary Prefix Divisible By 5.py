class Solution(object):
    def prefixesDivBy5(self, nums):
        result = []
        current = 0
        
        for bit in nums:
            # Shift left (multiply by 2) and add the new bit
            current = (current * 2 + bit) % 5
            # Check divisibility by 5
            result.append(current == 0)
        
        return result
        