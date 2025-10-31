import time
import random

def timer(func):
   
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' ran in: {execution_time:.6f} seconds")
        return result
    return wrapper

@timer
def fast_list_comprehension(n):
    return [i * i for i in range(n)]

@timer
def slower_for_loop(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

@timer
def math_intensive_function(n):
    data = [random.random() * 100 for _ in range(n)]
    result = []
    for x in data:
        result.append(math.sin(math.sqrt(x)) * math.log(x + 1))
    return result

import math
N = 1000000  

print(f"--- Running comparisons for N = {N} operations ---")

print("\nComparing List Creation Methods:")
fast_list_comprehension(N)
slower_for_loop(N)

print("\nComparing Simple vs. Intensive Calculation:")
N_SMALL = 100000 

fast_list_comprehension(N_SMALL)
math_intensive_function(N_SMALL)