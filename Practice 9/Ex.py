"""
print("Программа работа пароля")
password = ""
TRUE_PASSWORD = "1234"
while password != TRUE_PASSWORD:
    password = input('Пароль:')
print("Вы угадали пароль!")
"""
from itertools import count

from pygments.lexer import words

"""
print("Программа валидации возраста")
age_valid = False

while age_valid==False:
    age = int(input("Введите возраст: "))
    if 0<=age<120:
        age_valid = True
        print('Валидный возраст')
    else: print("Вы вампир")
"""
"""
print("Программа: Угадай число\n")
import random
num = random.randint(1,100)
us_number = 0
count = 1

while us_number != num:
    try:
        us_number = int(input("Введите число: "))
    except ValueError:
        print("Ошибка! Введено некорректное значение!")
    else:
        if us_number > num:
            print("Ваше число больше")
        elif us_number < num:
            print("Ваше число меньше")
        else:
            print("Вы угадали")
            print(f"Ваше количество попыток: {count}")
        count += 1
"""
"""
def word_count (ref):
    ref = 0
    print("Последовательность слов")
    count = 0
    word = ""
    while True:
        word = input("Введите слово: ")
        count += 1
        if word == "стоп" or word == "хватит" or word == "достаточно":
            break
    print(f"Конечное колличество слов равно: {count:g}")
word_count(12)
"""
print(25//10)