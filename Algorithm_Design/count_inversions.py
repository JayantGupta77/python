def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])

        merged, inv_split = merge(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        merged = []
        i = j = 0
        inversions = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    _, total_inversions = merge_sort(arr)
    return total_inversions

arr = [8, 4, 2, 1]
print(count_inversions(arr))
