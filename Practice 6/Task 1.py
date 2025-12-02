"""
Задание №1

"""
temp=int(input("Введите температуру вашего тела (C): "))
pressure = int(input("Введите ваше давление (верхнее): "))
pulse = int (input("Введите ваш пульс (уд/мин): "))

if temp !=range(35,38) or pressure !=range(105,140) or  pulse != range(55,110):
    print("Требуется врач!")
elif temp == range (35,36) or temp == range (37,38)  or pressure == range (105, 110) or pressure == range (130, 140) or pulse == range (55, 60)  or pulse == range (100, 110) :
    print("Легкое недомогание.")
elif temp == range (36,37) or pressure == range (110, 130)  or pulse == range (60, 100):
    print("Нормальное состояние.")
else: print("Введены некоректные данные.")