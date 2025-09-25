def sort_by_frequency(arr):
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    sorted_items = sorted(freq_map.items(), key=lambda x: (x[1], x[0]))

    sorted_arr = []
    for value, freq in sorted_items:
        sorted_arr.extend([value] * freq)

    return sorted_arr

arr = [4, 5, 6, 5, 4, 3]
sorted_arr = sort_by_frequency(arr)
print("Sorted by frequency:", sorted_arr)