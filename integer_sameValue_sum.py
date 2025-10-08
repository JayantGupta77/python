from itertools import combinations_with_replacement

def find_combinations(target_sum, num_elements, min_val=1, max_val=None):
    
    if max_val is None:
        max_val = target_sum
    
    numbers = range(min_val, max_val + 1)
    valid_combinations = []

    for combo in combinations_with_replacement(numbers, num_elements):
        if sum(combo) == target_sum:
            valid_combinations.append(combo)

    return valid_combinations

target = 10
count = 3

results = find_combinations(target, count)
print(f"Combinations of {count} integers that sum to {target}:")
for r in results:
    print(r)
