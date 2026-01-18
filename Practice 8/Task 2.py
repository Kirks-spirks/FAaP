out_print_title = ("первое","второе","третье","четвертое","пятое","шестое","седьмое","восьмое","девятое","десятое")
Pok = "Yes"
for i in range(10):
    inp_num = float(input(f"Введите {out_print_title[i]} число: "))
    if inp_num % 2 != 0:
      Pok = "No"
print("\nВсе числа четные:",Pok)