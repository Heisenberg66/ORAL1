import random

#list(set(list1).intersection(list2))
#elements communs de deux listes

A faire : 
- stats numéro communs
- gains

def tirage ():
    t = []
    for _ in range(5):
        r= random.randint(1,49)
        while r in t:
            r= random.randint(1,49)
        t.append(r)
    t.append(random.randint(1,10))
    return t


def jouer (grille):
    i=1
    t= tirage()
    chance_grille =grille[-1] 
    chance_tirage = t[-1]
    grille.pop()
    t.pop()
    grille.sort()
    t.sort()
    
    while t != grille or chance_grille!=chance_tirage:
        t=tirage()
        chance_tirage = t[-1]
        t.pop()
        t.sort()
        i+=1
        if i%100000==0:
            print("*", end="")
    print("\n")
    return i
        
    











# lst = []
# print("Compléter votre grille : \n")
# for i in range(1,6):
#     n=0
#     while int(n)<1 or int(n)>49 or int(n) in lst :
#         n = input("Numéro "+str(i)+" entre 1 et 49 : \n")
#     lst.append(int(n))
#     n=0
# while int(n)<1 or int(n)>10:
#     n=input("le numéro complémentaire entre 1 et 10 : \n") 
# lst.append(int(n))
    
lst=[42,23,16,15,8,4]
print(jouer(lst))
