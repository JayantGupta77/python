def product_of_negatives(numbers):
 
  negative_product = 1
  found_negative = False

  for num in numbers:
    if num < 0:
      negative_product *= num
      found_negative = True
  
  return negative_product if found_negative else 1

my_list = [2, -3, 4, -5, 6, -1]
result = product_of_negatives(my_list)
print(f"The list is: {my_list}")
print(f"The product of the negative numbers is: {result}") 

my_list_2 = [1, 2, 3, 4]
result_2 = product_of_negatives(my_list_2)
print(f"\nThe list is: {my_list_2}")
print(f"The product of the negative numbers is: {result_2}")