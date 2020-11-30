#while23
A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))
if B!=0 and A<B:
    НОД = A%B
if B!=0 and B<A:
    НОД = B%A
if B == 0:
    НОД == A
print('Наибольший общий делитель:', НОД)



