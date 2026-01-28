"""
s = 0
for i in range(1,100):
    s = s+i
print(s)
from rich.console import Console
from rich.panel import Panel

console = Console()


console.print(Panel("Статус вашего заказа".center(75), border_style="white"))
!!!
print("Перевод из 100-бальной в 5-бальную шкалу оценивания")
mark = int(input("Введите свой балл:"))
if mark>100 or mark<0:
    print("Ошибка ввода")
elif mark>=90:
    print("Ваша оценка 5 (отлично)\n")
elif mark>=75:
    print("Ваша оценка 4 (хорошо)\n")
elif mark>=60:
    print("Ваша оценка 3 (удовлетворительно)\n")
elif mark<60:
    print("Ваша оценка 2 (неудовлетворительно)\n")

### Task 3
def partyclubcheck (age, document, membership):

    Реализует фейсконтроль.
    :param age (float): Возраст проверяемого.
    :param document (boolean): Показывает наличие или отсутвие документа подтверждающего личность.
    :param membership (boolean): Показывает наличие или отсутвие документа о членстве в клубе.

    if (document == "Да" and age>=18) or (membership == "Да"):check = "Проходите"
    else: check = "Вход запрещен"
    print(check)
    return check
print("Фейсконтроль")
partyclubcheck(int(input("Введите вас возраст: ")), str(input("Введите, есть ли у вас документ, подтверждающий личность(Да/Нет): ")), str(input("Введите, есть ли у вас членство в клубе (Да/Нет): ")))
help(partyclubcheck)
"""
"""
print("Сумма чисел введеных пользователем")

total_user_num = 0

while True:
    try:
        user_num = int(input("Введите целое число: "))
    except ValueError:
        print("Ошибка, введено некорректное значение")
    else:
        if user_num == 0:
            break
        total_user_num += user_num

print(f"Сумма чисел введеных пользователем: {total_user_num}")
"""