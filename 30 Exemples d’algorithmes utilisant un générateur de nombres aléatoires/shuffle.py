import random

def shuffle(liste):
    for i in range(len(liste)-1):
        r = random.randint(i+1,len(liste)-1)
        liste[i],liste[r]=liste[r],liste[i]
        

l = list(range(40))
print(l)
shuffle(l)
print(l)
print(l.shuffle())