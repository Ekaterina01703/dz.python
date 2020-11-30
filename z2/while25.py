#while25
N = int(input('Введите число,большее 1:'))
F1 = F2 = 1

while F2 <= N:
    F1,F2 = F2, F1+F2
    print(F2, end='; ')
print()
print('Первое число Фибоначчи,большее N:', F2)
