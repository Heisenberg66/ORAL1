# pgcd exotique
import random

def pgcd(b, a):
    cummul = 1
    while b != a and a != 1 and b != 1:
        if a%2 == 0 and b%2 == 0:
            a = a // 2
            b = b // 2
            cummul = cummul*2
        elif a%2 == 0:
            a = a // 2
        elif b%2 == 0:
            b = b // 2
        else:
            if a > b:
                a = a - b
            else:
                b = b - a
    return cummul*min(a, b)
    
a = 3*3*3*5*7*7*13
b = 2*2*3*5*7*11*17
print((a, b))
print(pgcd(a, b))
print(3*5*7)

a = random.randint(1000000, 10000000)
b = random.randint(1000000, 10000000)
print((a, b))
print(pgcd(a, b))
# complexite ????