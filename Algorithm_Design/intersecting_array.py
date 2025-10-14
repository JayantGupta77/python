def intersect_arrays(a, b):
    return list(set(a) & set(b)) 

a = [1, 2, 1, 3, 1]
b = [3, 1, 3, 4, 1]
print(intersect_arrays(a, b))  
