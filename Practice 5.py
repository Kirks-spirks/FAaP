month_income =float(input("Введите свой годовой доход: "))

TAX_BIT = 0.13
MONTH_AMOUNT = 12

all_income = month_income*MONTH_AMOUNT
tax_value = all_income*TAX_BIT
amount_after_taxes = all_income - tax_value - tax_value

print(f"Общий годовой доход составляет: {all_income:.2f}")
print(f"Общий годовой доход составляет: {tax_value:.2f}")
print(f"Общий годовой доход составляет: {amount_after_taxes:.2f}")









