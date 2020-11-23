#proc8
import random

def AddRightDigit(D):
    global K
    K = D+K*10

K = random.randrange(1,100)
print("Число K: ", K)

for i in range(2):
    D = random.randrange(0,10)
    print("Число D",i+1,": ", D)
    AddRightDigit(D)
print("Измененное K: " , K)
