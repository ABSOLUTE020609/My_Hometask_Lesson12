def calculate_rectangle_area(length, width):
    area = length * width
    return area

print(calculate_rectangle_area(3, 4))
print(calculate_rectangle_area(5, 5))
print(calculate_rectangle_area(10, 2))
print(calculate_rectangle_area(0, 5))
print(calculate_rectangle_area(8, 0))

print('-'*100)
def check_2_or_1(number):
    if number % 2 == 0:
        return "чётное"
    else:
        return "нечетным"

print(check_2_or_1(6))
print(check_2_or_1(0))
print(check_2_or_1(11))
print(check_2_or_1(20))
print(check_2_or_1(15))