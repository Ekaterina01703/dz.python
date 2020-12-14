#Array82
import random
N = random.randrange(2,10)
K = random.randrange(1,N)
print('N = ',N)
print('K = ',K)

A = [i+1 for i in range(N)]
print('Массив:',A)

for i in range(0,N-K):
    A[i]= A[i+K]
for i in range(N-K,N):
    A[i]=0
print('Итоговый массив:',A)

