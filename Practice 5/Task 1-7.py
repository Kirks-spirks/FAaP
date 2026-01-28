import math

### Task 1
month_income =float(input("Введите свой годовой доход: "))
TAX_BIT = 0.13
MONTH_AMOUNT = 12
all_income = month_income*MONTH_AMOUNT
tax_value = all_income*TAX_BIT
amount_after_taxes = all_income - tax_value - tax_value
print(f"Общий годовой доход составляет: {all_income:.2f}")
print(f"Общий годовой доход составляет: {tax_value:.2f}")
print(f"Общий годовой доход составляет: {amount_after_taxes:.2f}")

### Task 2
height,weight  =map (float, input("Введите свой рост и вес: ").split())
bmi = weight/(height*height)
print(f"Ваш индекс массы тела: {bmi:.2f} ")

### Task 3
def convert_usd_to_rub(amount_usd):
    """
    :param amount_usd:
    :return:
    """
    DOLLAR_EX_RATE=78.05
    return amount_usd*DOLLAR_EX_RATE
dollar_sum=float(input("Введите сумму для перевода в $: "))
print(f"Сумма в ₽ равна: {convert_usd_to_rub(dollar_sum):.3f} ")

### Task 4
def calculate_rectangle_area(width, height):
    """
    :param width:
    :param height:
    :return:
    """
    rectangle_area=width*height
    return rectangle_area
def calculate_circle_area(radius):
    """
    :param radius:
    :return:
    """
    circle_area=2*math.pi*radius
    return circle_area
width_out = float(input("Введите длинну прямоугольника: "))
height_out = float(input("Введите высоту прямоугольника: "))
radius_out = float(input("Введите радиус окружности: "))
print(f"Площадь прямоугольгика равна: {calculate_rectangle_area(width_out, height_out):.2f}")
print(f"Площадь круга равна: {calculate_circle_area(radius_out):.2f}")

### Task 5
def atm (cash_sum):
    print("bgv")

### Task 6
def calculate_distance(x1, y1, x2, y2):
    """
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    return math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))

def calculate_triangle_area(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    p=(a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))







































