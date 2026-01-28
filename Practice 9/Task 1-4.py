task_num=int(input("Введите номер задания (от 1 до 4): "))
match task_num:

    case 1:
        print("Задание №1 «Следуй правилам»")
        finish_num = int(input("Введите конечное натуральное число: "))
        i = 0
        while i<finish_num:
            i+=1
            if i in range(5,10) or i in range(17,38) or i in range(78,88):
                continue
            print(i)

    case 2:
        print("«Заданик №2 Сколько ждать?»")
        i = 0
        first_num = 0
        second_num = 0
        while True:
            i+=1
            name = str(input("Введите имя (в Именительном падеже): "))
            if name == "Александра" :
                first_num = i
            if name == "Левон":
                second_num = i
                break
        print(f"Количество людей между Александрой и Левоном: {second_num - (first_num + 1 )}")

    case 3:
        print("Задание №3 «Ведьмаку заплатите чеканной монетой»")
        order_cast = int(input("Введите цену за услугу ведьмака: "))
        flag = False
        quan_coin=0
        while not flag:
            if order_cast >=25:
                order_cast -= 25
                quan_coin+=1
            elif order_cast >=10:
                order_cast -= 10
                quan_coin+=1
            elif order_cast >=5:
                order_cast -= 5
                quan_coin+=1
            elif order_cast >=1:
                order_cast -= 1
                quan_coin+=1
            else: flag = True
        print(f"Количество монет за заказ: {quan_coin}")

    case 4:
        print("Задание №4 «Все вместе»")
        enter_num=int(input("Введите натуральное число: "))
        count_three=0
        count_last=0
        count_even=0
        sum_more_five=0
        prod_more_seven=1
        null_and_five=0
        last_num=enter_num%10
        while enter_num!=0:
            proc_numeral=enter_num%10
            enter_num = enter_num//10
            if proc_numeral==3: count_three+=1
            if proc_numeral==last_num: count_last+=1
            if proc_numeral%2==0: count_even+=1
            if proc_numeral>5: sum_more_five+=proc_numeral
            if proc_numeral>7: prod_more_seven=proc_numeral*prod_more_seven
            if proc_numeral==0 or proc_numeral ==5: null_and_five+=1
        print(f"В числе встречается {count_three} цифр три\n"
              f"Последняя цифра встречается в числе {count_last} раз\n"
              f"В числе {count_even} чётных цифр\n"
              f"Сумма его цифр, больших пяти равна {sum_more_five}\n"
              f"Произведение цифр числа, больших семи: {prod_more_seven}\n"
              f"Цифры 0 и 5 встречаются в числе {null_and_five} раз")





