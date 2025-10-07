def sum_of_digits(number):
    number = abs(number)
    digit_sum = 0

    while number > 0:
        last_digit = number % 10
        
        digit_sum += last_digit
        
        number = number // 10
        
    return digit_sum

num = 478
result = sum_of_digits(num)

print(f"The number is: {num}")
print(f"The sum of its digits is: {result}") 

num2 = 10001
result2 = sum_of_digits(num2)
print(f"\nThe number is: {num2}")
print(f"The sum of its digits is: {result2}")