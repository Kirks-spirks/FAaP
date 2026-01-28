"""
Задание №1 Диагностика состояния здоровья

"""
from random import choices


def Health_monitor ():
    print("Мониторинг состояния здоровья")
    temp = int(input("Введите температуру вашего тела (C): "))
    pressure = int(input("Введите ваше давление (верхнее): "))
    pulse = int(input("Введите ваш пульс (уд/мин): "))

    if 36 <= temp <= 37  and 110 <= pressure <=130 and 60 <= pulse <=100:
        print("Нормальное состояние.")
    elif 35 <= temp < 36 or 37 < temp <= 38  or 105 <= pressure < 110 or 130 < pressure <= 140 or 55<= pulse < 60 or 100 < pressure <= 110 :
        print("Легкое недомогание.")
    elif 35 < temp < 38 or 105 < pressure <140 or  55 < pulse < 110:
        print("Требуется врач!")
    else: print("Введены некоректные данные.")

"""
Задание №2 Цвета колеса рулетки

"""
def Wheel_color ():
    print("Цвета колеса рулетки")
    pocket_number = int(input("Введите номер кармана: "))
    if pocket_number == 0:
        print("Зеленый")
    elif (0 < pocket_number <= 11):
        if pocket_number % 2 == 0:
            print("Черный")
        else:
            print("Красный")
    elif (11 < pocket_number <= 18):
        if pocket_number % 2 == 0:
            print("Красный")
        else:
            print("Черный")
    elif (19 < pocket_number <= 28):
        if pocket_number % 2 == 0:
            print("Черный")
        else:
            print("Красный")
    elif (29 < pocket_number <= 36):
        if pocket_number % 2 == 0:
            print("Красный")
        else:
            print("Черный")
    else: print("Введены некоректные данные")

"""
Задание №3 Шахматная доска

"""
def Chess_board ():
    print("Шахматная доска")
    line_1,colums_1 =map(int(input("Введите номер столбца и строки первой клетки через пробел: ")))
    line_2,colums_2 =map(int(input("Введите номер столбца и строки второй клетки через пробел: ")))
    if (line_1+colums_1)%2 == (line_2+colums_2)%2:
        print("YES")
    else:
        print("NO")

"""
###Задание №4 Ход слона

"""
def Eledant_turn():
    print("Ход слона")
    line_1,colums_1 =map(int(input("Введите номер столбца и строки первой клетки через пробел: ")))
    line_2,colums_2 =map(int(input("Введите номер столбца и строки второй клетки через пробел: ")))
    if line_1+colums_1 == line_2+colums_2:
        print("YES")
    else:
        print("NO")

"""
###Задание №5 Ход ферзя

"""
def Qween_turn():
    print("Ход королевы")
    line_1, colums_1 = map(int(input("Введите номер столбца и строки первой клетки через пробел: ")))
    line_2, colums_2 = map(int(input("Введите номер столбца и строки второй клетки через пробел: ")))
    if (line_1 + colums_1 == line_2 + colums_2) or (line_1 == line_2 or colums_1 == colums_2):
        print("YES")
    else:
        print("NO")

choice =int(input("Введите номер задания (от 1 до 5): "))
match choice:
    case 1: Health_monitor()
    case 2: Wheel_color()
    case 3: Chess_board()
    case 4: Eledant_turn()
    case 5: Qween_turn()


