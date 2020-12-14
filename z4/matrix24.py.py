#Matrix24
import random
import numpy as np

M = random.randrange(1,5)
N = random.randrange(1,5)
print('M = ',M)
print('N = ',N)
A = np.random.randint(7,size=(M,N))
print('Матрица:',A)
for i in range(N):
    x = A[:,i]
    print('Столбец:',x)
    print('Максимум:',max(x))