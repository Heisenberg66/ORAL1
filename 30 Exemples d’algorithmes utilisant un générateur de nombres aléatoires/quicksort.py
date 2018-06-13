import random

def tri_rapide(tableau):
    if  not tableau:
        return []
    else:
        pivot = tableau[random.randint(0,len(tableau)-1)]
        plus_petit = [x for x in tableau     if x <  pivot]
        plus_grand = [x for x in tableau if x > pivot]
        return tri_rapide(plus_petit) + [pivot] + tri_rapide(plus_grand)
 
        
liste = [3,56,47,39,82,2,0,40,23]
print(tri_rapide(liste))
