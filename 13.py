import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return "Phương trình vô nghiệm" if c != 0 else "Phương trình có vô số nghiệm"
        else:
            return f"Nghiệm của phương trình là: x = {-c / b}"

    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    elif discriminant == 0:
        x = -b / (2 * a)
        return f"Có 1 nghiệm kép: x = {x}"
    else:
        return "Phương trình vô nghiệm"

try:
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))

    result = solve_quadratic(a, b, c)
    print(result)

except ValueError:
    print("Vui lòng nhập vào các số hợp lệ.")
print("THÁI QUANG DUY") 
