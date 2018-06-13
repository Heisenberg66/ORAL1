import numpy 
import random
            
# génération des coordonnées de toutes les cases
def genere_coordonnees():
    cases = []
    for i in range(8):
        for j in range(8):
            cases.append((i,j))
    return cases

   
# suppression des cases de la ligne i
def suppr_ligne(i):
    # mémorisation des cases
    suppr = []
    
    # recherche
    for k in cases:
        if k[0]==i:
            suppr.append(k)
    # suppression
    for z in suppr:  
        if z in cases:
            cases.remove(z)
    
# suppression des cases de la colonne j 
def suppr_colonne (j):
    # mémorisation
    suppr = []
    
    #recherche
    for k in cases:
        if k[1]==j:
            suppr.append(k)
    
    # suppression
    for z in suppr:  
        if z in cases:
            cases.remove(z)

# suppression des cases des diagonales passant par la case de coordonnées (i,j)
def suppr_diagonale (i,j):
    l1=i-1
    c1=j-1
    l2=i+1
    c2=j+1
    # tant qu'une diagonale n'est pas finie
    while (l1>=0 and c1 >= 0) or (l1>=0 and c2<=7) or (l2<=7 and c2 <=7) or (l2<=7 and c1>=0):
        
        if l1>=0:
            if c1>=0:
                if (l1,c1) in cases:
                    cases.remove((l1,c1))
                
            if c2<=7:
                if (l1,c2) in cases:
                    cases.remove((l1,c2))

        
        if l2<=7:
            if c1>=0:
                if (l2,c1) in cases:
                    cases.remove((l2,c1))
                
            if c2<=7:
                if (l2,c2) in cases:
                    cases.remove((l2,c2))
        l1-=1
        c1-=1
        l2+=1
        c2+=1
       

# echequier pour visualisation 
def visualisation ():  
    echequier=numpy.zeros((8,8),dtype='int')
    for coordonnees in reines:
        echequier[coordonnees[0],coordonnees[1]]=1
    return echequier
    
    
    
     
reines = []  
nb_essai = 0
# tant qu'on arrive pas a placer nos huit reines
while len(reines)<8:
    reines = []   # coordonnées des reines
    cases = genere_coordonnees() # les 64 coordonnées de l'échequier
    k=0 # nombre de reines placé
    
    # tant qu'il reste des cases et que moins de 8 reines sont placées
    while len(cases)>0 and k<8:
    
        # randint entre 1 et nombre de cases possibles restantes
        rand = random.randint(0,len(cases)-1)

        # sauvegarder la position de la reine
        reines.append(cases[rand])
    
        # i : ligne ; j : colonne
        i=cases[rand][0]
        j=cases[rand][1]
    
        # remplissage de l'éche
        suppr_ligne(i)
        suppr_colonne(j)
        suppr_diagonale(i,j)
    
        k+=1
    nb_essai+=1
    
print(visualisation())
print("Nombre d'essai : "+str(nb_essai))