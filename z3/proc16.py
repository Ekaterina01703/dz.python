#proc16
import random

def Sign(X):
    if X<0:
        return(-1)
    if X==0:
        return(0)
    if X>0:
        return(1)
A = random.randrange(-5,5)
B = random.randrange(-5,5)
print('A = ', A)
print('B = ', B)
print('Sign(A)=',Sign(A))
print('Sign(B)=',Sign(B))

S_A = Sign(A)
S_B = Sign(B)

result = S_A + S_B
print('Sign(A) + Sign(B) = ', result)
