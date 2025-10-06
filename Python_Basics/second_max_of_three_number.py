def second_max(a, b, c):
    nums = [a, b, c]
    nums.sort()
    return nums[1]

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print("Second largest number is:", second_max(a, b, c))