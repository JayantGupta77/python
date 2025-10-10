def is_divisible_by_3(number):
  
  if number % 3 == 0:
    return True
  else:
    return False


num1 = 9
num2 = 10
num3 = 0
num4 = -6

print(f"{num1} is divisible by 3: {is_divisible_by_3(num1)}")
print(f"{num2} is divisible by 3: {is_divisible_by_3(num2)}")
print(f"{num3} is divisible by 3: {is_divisible_by_3(num3)}")
print(f"{num4} is divisible by 3: {is_divisible_by_3(num4)}")