def linear_hash_sort(arr):
    size = len(arr) * 2
    hash_table = [None] * size

    for num in arr:
        index = num % size
        while hash_table[index] is not None:
            index = (index + 1) % size
        hash_table[index] = num

    sorted_arr = []
    for i in range(size):
        if hash_table[i] is not None:
            sorted_arr.append(hash_table[i])

    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key

    return sorted_arr

arr = [23, 12, 45, 9, 34, 12, 8]
sorted_arr = linear_hash_sort(arr)
print("Sorted array:", sorted_arr)