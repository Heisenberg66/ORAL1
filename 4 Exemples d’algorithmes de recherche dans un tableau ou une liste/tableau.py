import random as r

#-------------------------------------------------------------------------------
# ----------------- Algorithmes pour tableau non trié --------------------------
#-------------------------------------------------------------------------------

# Vérifie sur l'élément appartien au tableau
# Complexité : O(i)
def est_present(l,val):
    i=0
    while i<len(l):
        if l[i]==val:
            return True
        i+=1
    return False


#-------------------------------------------------------------------------------


# renvoie la position de l'élément si il est dans le tableau
# complexité : O(i)
def position (l,val):
    i=0
    while i<len(l):
        if l[i]==val:
            return i
        i+=1
    return -1

    
#-------------------------------------------------------------------------------    

    
# renvoie l'élément à la postion i
# complexité : O(1)
def a_la_position(l,i):
    return l[i]


#-------------------------------------------------------------------------------


# cherche le nombre d'occurence d'un objet
# complexité  : O(n)
def occurence(l,val):
    occ= 0
    for i in l:
        if i==val:
            occ+=1
    return occ


#-------------------------------------------------------------------------------


# renvoie la position des doublon d'un objet
# Complexité : O(n)
def doublon(l,val):
    doublon =list()
    for i in range(len(l)):
        if l[i]==val:
            doublon.append(i)
    return doublon

#-------------------------------------------------------------------------------


# renvoie le minimum d'un tableau ( éléments comparables)
# Complexité : O(n)
def min(l):
    if not l:
        return None
    min = l[0]
    for i in l:
        if i<min:
            min=i
    return min
 
#------------------------------------------------------------------------------- 
 
# renvoie le maximum d'un tableau ( éléments comparables)
# Complexité : O(n)   
def max(l):
    if not l:
        return None
    max = l[0]
    for i in l:
        if i>max:
            max=i
    return max


#-------------------------- Recherche auto adaptative --------------------------

# recherche auto adaptive, avancé l'élement de 1
# on inverse les valeurs pour une complexité en 0(i)
def auto_methode1(l,val):
    if l[0] != val :
        i = 0
        while i<len(l)-1:
            if l[i+1]==val:
                l[i],l[i+1]=l[i+1],l[i]
                break
            i+=1

# recherche auto adaptative, avancé l'élément en première position
# complexité O(i) (recherche)
#           + O(n-i) (suppression donc décalage de 1 vers la gauche des n-i éléments suivant l[i]
#           + O(n) (ajout en tête de tableau donc décalage de 1 des n éléments suivant vers la droite
def auto_methode2(l,val):
    if l[0] != val:
        i=0
        while i<len(l):
            if l[i]==val:
                tmp = l[i]
                del l[i]
                l.insert(0,tmp)
                break
            i+=1


#-------------------------------------------------------------------------------
# ----------------- Algorithmes pour tableau triée --------------------------
#-------------------------------------------------------------------------------


def est_present2(l,val):
    i=0
    while i<len(l) and l[i]<=val:
        if l[i]==val:
            return True
        i+=1
    return False

    
#-------------------------------------------------------------------------------


def position2(l,val):
    i=0
    while i<len(l) and l[i]<=val:
        if l[i]==val:
            return i
        i+=1
    return -1


#-------------------------------------------------------------------------------


def occurence2(l,val):
    i=0
    occ=0
    while i<len(l) and l[i]<=val:
        if l[i]==val:
            occ+=1
        i+=1
    return occ


#-------------------------------------------------------------------------------


def doublons2(l,val):
    i=0
    doublon=[]
    while i<len(l) and l[i]<=val:
        if l[i]==val:
            doublon.append(i)
        i+=1
    return doublon
    
    
#-------------------------------------------------------------------------------


def min2(l):
    return l[0]
    
    
#-------------------------------------------------------------------------------


def max2(l):
    return l[-1]

#-------------------------------- Dichotomie -----------------------------------


def dichotomie_iter(l,val):
    debut =0
    fin = len(l)
    
    while fin>=debut:
        mediane = (fin+debut)//2
        print(l[debut:fin+1])
        if l[mediane]==val:
            return mediane
        elif l[mediane]>val:
            fin = mediane-1
        elif l[mediane]<val:
            debut = mediane+1
    return None

 
def dichotomie_recursif(l,val):
    if len(l)>0:
        print(l)
        mediane = len(l)//2
        if l[mediane]==val:
            return True
        elif l[mediane]>val:
            return dichotomie_recursif(l[:mediane],val)
        elif l[mediane]<val:
            return dichotomie_recursif(l[mediane+1:],val)
    return False
    


#-------------------------------------------------------------------------------            
#---------------------------------- MAIN ---------------------------------------
#-------------------------------------------------------------------------------    

if __name__ == "__main__" :
    l = list(range(40))
    r.shuffle(l)
    l1 = list(range(0,40,2))
    print(dichotomie_recursif(l1,8))
    