def is_scalene(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a != b and b != c and a != c:
            return True
        else:
            return False
    else:
        return False

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if is_scalene(a, b, c):
    print("The triangle is scalene.")
else:
    print("The triangle is not scalene.")