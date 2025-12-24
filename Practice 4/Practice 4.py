import math

### Task 1
print("Task 1")
number = float(input("Введите число: "))
number = math.floor(number)+math.ceil(number)
print(f"Сумма округления числа в большую и меньшую сторону равна: {number}\n")

### Task 2
print("Task 2")
x1 = float(input("Введите координаты x первой точки: "))
y1 = float(input("Введите координаты y первой точки: "))
x2 = float(input("Введите координаты x второй точки: "))
y2 = float(input("Введите координаты y второй точки: "))
distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(f"Евклидово расстояние между точками равно: {distance} \n")

### Task 3
print("Task 3")
try:
    number_1=int(input("Введите число: "))
    number_str=str(number_1)
    print(number_str[0])
    print(number_str[1])
    print(number_str[2])
    print(f"{number_str[3]} \n")
except IndexError: print("Введенные данные некоректны.")

### Task 4
print("Task 4")
sholar_n =int(input("Введите количество школьников: "))
mandarin_k = int(input("Введите количество мандаринов: "))
print(f"Количество мандаринов у каждого школьника = {mandarin_k//sholar_n}")
print(f"Количество мандаринов,оставшихся в корзине = {mandarin_k%sholar_n}\n")

### Task 5
print("Task 5")
minute_orig = int(input("Введите исходное кол-во минут: "))
hour = minute_orig//60
minute = minute_orig%60
print(f"{minute_orig} мин - это {hour} часа и {minute} минут.\n")

### Task 6
print("Task 6")
degrees_x=float(input("Введите число градусов: "))
trig_meaning = math.sin(degrees_x)+math.cos(degrees_x)+(math.tan(degrees_x))**2
print(f"Значение выражения sin x+cos x+tg^2 при заданных значениях = {trig_meaning}\n")

### Task 7
print("Task 7")
