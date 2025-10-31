def largest_divisible_subset(nums):
    if not nums: return []
    nums.sort()
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    max_idx = 0

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[i] > dp[max_idx]:
            max_idx = i

    # Reconstruct subset code
    result = []
    while max_idx != -1:
        result.append(nums[max_idx])
        max_idx = prev[max_idx]
    return result[::-1]

# Example usage:
nums = [1, 2, 4, 8, 16]
print(largest_divisible_subset(nums))
