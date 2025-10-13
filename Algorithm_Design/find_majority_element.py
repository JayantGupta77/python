def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return -1

arr = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(arr))  
