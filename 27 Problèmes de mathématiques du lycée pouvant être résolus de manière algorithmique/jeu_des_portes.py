import random as random

def jeu ():
    portes =[1,2,3]
    soluce = random.randint(0,2)
    choix = random.randint(0,2)
    
    return #True or False

def simulation (n):
    change= 0
    for _ in range(n):
        if jeu():
            change+=1
    return change/n
    
    