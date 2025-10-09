import math
def calculate_lcm(a, b):
    
    if a == 0 or b == 0:
        return 0
    
    greatest_common_divisor = math.gcd(a, b)
    
    lcm = abs(a * b) // greatest_common_divisor
    return lcm
num1 = 54
num2 = 24
gcd_result = math.gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}") 

lcm_result = calculate_lcm(num1, num2)

num3 = 17
num4 = 5
print(f"\nThe GCD of {num3} and {num4} is: {math.gcd(num3, num4)}") 
print(f"The LCM of {num3} and {num4} is: {calculate_lcm(num3, num4)}") 