#begin21
import math

x1,y1 = map(int,input('Введите координаты первой вершины:').split())
x2,y2 = map(int,input('Введите координаты второй вершины:').split())
x3,y3 = map(int,input('Введите координаты третьей вершины:').split())

a = math.sqrt((x2-x1)**2+(y2-y1)**2)
b = math.sqrt((x3-x2)**2+(y3-y2)**2)
c = math.sqrt((x1-x3)**2+(y1-y3)**2)

p =(a + b + c)/2
S = math.sqrt(p*(p - a)*(p - b)*(p - c))

print('Площадь:',S)
print('Периметр:',a+b+c)
