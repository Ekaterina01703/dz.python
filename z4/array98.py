#array98
import random
N = random.randrange(1,25)
print('N = ',N)
array = [random.randint(1,10) for i in range(N)]
print('Массив:',array)
i = 0
while i< len(array):
    x = array[i]
    k = 0
    for y in array:
        if x==y:
            k+=1
    if k <3:
        array.remove(x)
    else:
        i+=1
print('Полученный массив:',array)
print('Размер полученного массива:', len(array))

