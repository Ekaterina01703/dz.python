#for19
N = int(input('Введите целое число,большее 0:'))
print('N = ', N)
N_proizvedenie = 1
for i in range(1,N+1):
    N_proizvedenie *= i
print('Произведение равно:', N_proizvedenie)
