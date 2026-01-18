try:
    n = int(input("Введите натуральное число: "))
    for i in range(1,10):
        print(f"{n}*{i}={n*i}")
except ValueError:
    print("Введен неверный тип данных.")