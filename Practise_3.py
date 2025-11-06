#Задание №1
a = 42
b = 3.14556574
c = "Hello, World!"
d = True
e = [1, 2, 3]  #list
f = (4, 5, 6)  #tuple
g = {"name": "Alice", "age": 30}  #Mapping
h = {7, 8, 9}  #
i = None  #SpecialType
print(" переменная a это -", type(a), "\n", "переменная b это -", type(b), "\n",
      "переменная c это -", type(c), "\n", "переменная d это -", type(d), "\n",
      "переменная e это -", type(e), "\n", "переменная f это -", type(f), "\n",
      "переменная g это -", type(g), "\n", "переменная h это -", type(h), "\n",
      "переменная i это -", type(i), "\n")

#Задание №2
my_list = [1, 2, 3]
print(my_list)
my_list[0] = 100
print(my_list)

my_typle = (1, 2, 3)
print(my_typle)
#my_typle[0]=100
print(my_typle)

my_string = "cat"
print(my_string)
#my_string[0] = 'b'
print(my_string)

#Задание №3
print('Введите первое число')
num1 = input()
print('Введите второе число')
num2 = input()
try:
    amount = int(num1) + int(num2)
except ValueError:
    print("Введенные значения не коректны")
else:
    print(amount)

#Задание №4
print("Для хранения текущего количества студентов в группе лучше всего подходит переменная с типом данных float \n"
          "т.к ")

#Задание №5
shopping_list = ["Колбаса", "Курица", "Вишневый сок", "Картошка"]
print(shopping_list)
shopping_list.append("Лук")
print(shopping_list)
print(len(shopping_list))
unique_items = {"Колбаса", "Курица", "Вишневый сок", "Картошка", "Лук"}
print(unique_items)

#Задание №6
name = input("Введите ваше имя:")
age_str = input("Ваш возраст:")
