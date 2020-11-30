#for29
import random
N = int(input('Введите число,большее 1:'))
print('N = ', N )

B = random.randrange(1,10)
print('B = ', B)
A = random.randrange(0,B)
print('A = ', A)

H = (B - A)/N
print('H = ',round(H,1))

X = A
for i in range(0,N):
    print(round(X,1), end=',')
    X+=H
print(round(X,1),',',B)

