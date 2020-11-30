#series12
import random
x = int(input('Введите х,большее 0:'))
print(x,end='; ')
k = 0
while x != 0:
    x = random.randrange(-3,4)
    print(x,end='; ')
    k+=1
print()
print('Количество чисел в наборе:', k)
    
