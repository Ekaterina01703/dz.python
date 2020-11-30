#if13
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a < b and b < c:
    print('Среднее число: ', b)
if b < c and c < a:
    print('Среднее число: ', c)
if c < a and a < b:
    print('Среднее число: ', a)
if c < b and b < a:
    print('Среднее число: ', b)
if a < c and c < b:
    print('Среднее число: ', c)
if b < a and a < c:
    print('Среднее число: ', a)
