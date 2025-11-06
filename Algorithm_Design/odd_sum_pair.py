def count_odd_sum_pairs(arr):
    cnt_even = sum(1 for x in arr if x % 2 == 0)
    cnt_odd = len(arr) - cnt_even
    return cnt_even * cnt_odd

arr = [1, 2, 3, 4, 5]
result = count_odd_sum_pairs(arr)
print("Number of odd sum pairs:", result)
