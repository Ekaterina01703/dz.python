#minmax8
import random
N = random.randrange(2,20)
print('N = ',N)
array = [random.randint(1,5) for i in range(N)]
print(array)
min_val = min(array)

for i in range(len(array)):
    if array[i]==min_val:
        idx_first_min = i
print('Индекс первого минимума:',idx_first_min)
for i in range(len(array)):
    if array[i-1]==min_val:
        idx_last_min = i
print('Индекс последнего минимума:',idx_last_min)

