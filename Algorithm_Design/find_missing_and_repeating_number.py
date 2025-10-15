def find_missing_and_repeating(arr):
    n = len(arr)
    count = [0] * (n + 1)
    repeating = -1
    missing = -1
    for num in arr:
        count[num] += 1
    for i in range(1, n + 1):
        if count[i] == 2:
            repeating = i
        elif count[i] == 0:
            missing = i
    return repeating, missing

arr = [3, 1, 2, 5, 3]
repeat, miss = find_missing_and_repeating(arr)
print("Repeating number:", repeat)
print("Missing number:", miss)
