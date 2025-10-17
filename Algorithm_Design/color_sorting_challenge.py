def sortColors(nums):
    start, mid, end = 0, 0, len(nums) - 1

    while mid <= end:
        if nums[mid] == 0:
            nums[start], nums[mid] = nums[mid], nums[start]
            start += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            
            nums[mid], nums[end] = nums[end], nums[mid]
            end -= 1

nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  
