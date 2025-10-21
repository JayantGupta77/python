numbers = [4, 7, 2, 7, 9, 2, 5]
target = 7
if target in numbers:
    index = numbers.index(target)
    print(f"First occurrence of {target} is at index {index}")
else:
    print(f"{target} not found in the list")