def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

arr = [2, 3, 1, 5]
print(find_missing_number(arr))  
