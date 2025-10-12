import math
def find_largest_and_second_largest_single_pass(data_list):
    
    largest = -math.inf
    second_largest = -math.inf
    
    for number in data_list:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    if largest == -math.inf:
        return None, None
    if second_largest == -math.inf:
        return largest, None
        
    return largest, second_largest

numbers = [8, 3, 15, 1, 15, 6]
largest, second_largest = find_largest_and_second_largest_single_pass(numbers)

print(f"\nOriginal List: {numbers}")
print(f"Largest (Single Pass): {largest}")
print(f"Second Largest (Single Pass): {second_largest}")