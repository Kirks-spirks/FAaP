height,weight  =map (float, input("Введите свой рост и вес: ").split())
bmi = weight/(height*height)
print(f"Ваш индекс массы тела: {bmi:.2f} ")
