def search_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1  


arr = [12, 5, 8, 19, 3, 7]
target = 19

result = search_element(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")

    