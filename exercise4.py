# calculate sin, cos, sinh, cosh
def factorial(k):
    if k == 0 or k == 1:
        return 1
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result

def sin_approx(x, n):
    sin_x = 0
    for i in range(n):
        sign = (-1)**i
        sin_x += sign * (x**(2*i + 1)) / factorial(2*i + 1)
    return sin_x

def cos_approx(x, n):
    cos_x = 0
    for i in range(n):
        sign = (-1)**i
        cos_x += sign * (x**(2*i)) / factorial(2*i)
    return cos_x

def sinh_approx(x, n):
    sinh_x = 0
    for i in range(n):
        sinh_x += (x**(2*i + 1)) / factorial(2*i + 1)
    return sinh_x

def cosh_approx(x, n):
    cosh_x = 0
    for i in range(n):
        cosh_x += (x**(2*i)) / factorial(2*i)
    return cosh_x

# Input section
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số lần lặp muốn xấp xỉ (n): "))

# Output results
print(f"Ước lượng sin({x}) với n = {n} là: {sin_approx(x, n)}")
print(f"Ước lượng cos({x}) với n = {n} là: {cos_approx(x, n)}")
print(f"Ước lượng sinh({x}) với n = {n} là: {sinh_approx(x, n)}")
print(f"Ước lượng cosh({x}) với n = {n} là: {cosh_approx(x, n)}")
