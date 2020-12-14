#Matrix8
import random
import numpy

A = random.randrange(2,6)
M = random.randrange(2,6)
K = random.randrange(0,M)
print("A = ",A,"; M = ",M,"; K = ",K)
a = numpy.zeros((A, M))

for i in range(A):
    for j in range(M):
        a[i][j] = random.randrange(-5,5)
print(a)
print("Столбец ",K,": ")
for i in range(A):
    print(a[i][K],end="; ")
print()
