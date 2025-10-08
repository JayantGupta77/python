def generate_ap(a, d, n):
    
    return [a + i * d for i in range(n)]

first_term = 2
common_diff = 3
num_terms = 10

ap_sequence = generate_ap(first_term, common_diff, num_terms)
print("Arithmetic Progression:", ap_sequence)
