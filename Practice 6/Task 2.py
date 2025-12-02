"""
Задание №2

"""
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