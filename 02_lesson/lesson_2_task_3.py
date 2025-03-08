from math import ceil


def square(a):
    return ceil(a*a)


input_a = float(input("Длина стороны квадрата: "))
result = square(input_a)
print(f'Площадь квадрата - {result}')
