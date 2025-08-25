def print_multiplication_table(num):
   
    for i in range(1, 11):
        product = num * i
        print(f"{num} * {i} = {product}")

user_input = input("Enter a number to print its multiplication table: ")
try:
    a = int(user_input)
    print_multiplication_table(a)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")