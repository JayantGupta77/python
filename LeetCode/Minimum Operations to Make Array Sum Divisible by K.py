class Solution(object):
    def minOperations(self, nums, k):
        
        total_sum = sum(nums)
        
        remainder = total_sum % k
        
        if remainder == 0:
            return 0
        
        return remainder
        