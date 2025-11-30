
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

def partyclubcheck (age, document, membership):
    if (document == "Да" and age>=18) or (membership == "Да"):check = "Проходите"
    else: check = "Вход запрещен"
    print(check)
    return check
print("Фейсконтроль")
partyclubcheck(int(input("Введите вас возраст: ")), str(input("Введите, есть ли у вас документ, подтверждающий личность(Да/Нет): ")), str(input("Введите, есть ли у вас членство в клубе (Да/Нет): ")))