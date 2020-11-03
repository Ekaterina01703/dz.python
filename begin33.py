#begin33
ves_konf_X = int(input("Введите вес конфет Х:"))
ves_konf_Y = int(input("Введите вес конфет Y:"))

price_x_kg = 200
price_1kg = price_x_kg / ves_konf_X
price_y_kg = price_1kg * ves_konf_Y

print('Стоимость 1кг конфет:', price_1kg)
print('Стоимость Y кг конфет:', price_y_kg)
