### Task1
print("Task 1 ","Определение и исследование типов")
a = 42
b = 3.14159
c = "Hello,Python!"
d = True
e = [1,2,3]
f = (4,5,6)
g = {"name": "Alice","age":30}
h = {7,8,9}
i = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i),"\n")

### Task2
print("Task 2 ","Изменяемость и Неизменяемость" )
my_list = [1,2,3]
print(my_list)
my_list[0] =100
print(my_list) ### Список (list) является изменяемым массивом, который позволяет добавлять, удалять и изменять элементы.
my_tuple = (1,2,3)
print(my_tuple)
### my_tuple[0] = 100
### print(my_tuple)  Кортеж (typle) является неизменяемым списком, может хранить наборы констант или использоваться в качестве словарей, при попытке изменения выдает ошибку.
my_string = "cat"
print(my_string, "\n")
### my_string[0] ='b'
### print(my_string) Строка (string) является неизменяемым типом данных в Python

### Task3
print("Task 3 ","Преобразование типов")
try:
    num1 = (input("Введите 1-ое число: "))
    num2 = (input("Введите 2-ое число: "))
    num1 = int(num1)
    num2 = int(num2)
    print("Сумма 1-ого и 2-ого числа =",num1+num2)
except ValueError: print("Введенные данные некоректны.")

### Task4
print("\nTask 4 ","Выбор типа данных")
print("1-int, т.к. кол-во студентов является целочисленным числом")
print("2-float, т.к. температура является дробным числом")
print("3-str, т.к. логин является неизменяемой последовательностью символов, то есть строкой")
print("4-bool, т.к. информация о том, включено ли уведомление принимает два логических значения да/нет")
print("5-list, т.к. список любимых фильмов может меняться со временем")
print("6-tuple, т.к. по условию координаты не должны изменяться после задания")
print("7-set, т.к. ID товаров в корзине расположенны случайно")
print("8-dict ?mapping?, т.к. требуется пара данных, связанных между собой \n")

#### Task5
print("Task 5 ","Работа с коллекциями")
shopping_list = ["Морковь","Лосось","Лимон","Картофель"]
print(shopping_list)
shopping_list.append("Специи")
print(shopping_list)
unique_items = ("Морковь","Лосось","Лимон","Картофель\n")
print(unique_items) ### множество является неизменяеммым

#### Task6
print("Task 6")
name = input("Ваше имя: ")
age_str = input("Ваш возраст: ")
subjects_str = input("Любимые предметы (через запятую): ")
age_str = int(age_str)
student = {subjects_str}

print("\n=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)
print(f"Имя: {name}")
print(f"Возраст: {age_str}")
print(f"Любимые предметы: {subjects_str}")
print("=" * 30)