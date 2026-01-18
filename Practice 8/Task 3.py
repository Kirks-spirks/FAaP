n = int(input("Введите натуральное число: "))
sum = 0
for i in range(1,n+1):
    if i % 2 != 0:
        sum = sum+i
    else:
        sum = sum-i
print(f"\nЗнакопеременная сумма введенных чисел = {sum}")