#Series26
import random
K = random.randrange(0,10)
N = random.randrange(1,5)
print('K = ',K)
print('N = ',N)
for i in range(0,N):
    A = random.randrange(-10,11)
    A_K = 1
    for j in range(0,K):
        A_K*=A
    print('A = ',A)
    print('A^K =',A_K)
