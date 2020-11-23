#minmax24
import random
N = random.randrange(2,10)
print('N = ',N)
array = [random.randint(1,10) for i in range(N)]
print('Набор:',array)
for i in range(N):
    max_summ = array[0]+array[1]
for i in range(N-1):
    if array[i]+array[i+1]>max_summ:
        max_summ = array[i]+array[i+1]
print('Максимальная сумма двух соседних чисел:',max_summ)
