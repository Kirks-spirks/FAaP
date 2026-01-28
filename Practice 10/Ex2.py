
user_attempt = 3


while True:
    user_pass=str(input(f"Введите пароль (осталось {user_attempt} попыток): "))
    user_attempt-=1

    if user_pass=="admin":
        print("Доступ разрешен")
        break
    if user_attempt==0:
        print("Доступ заблокирован")
        break

prod = 1
while True:
    user_num=float(input("Введите число: "))
    if user_num>0:prod*=user_num
    elif user_num<0:break
print(f"Результат произведения: {prod}")