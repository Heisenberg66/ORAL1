from random import shuffle
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time


#------------------------------------------------------------------------------
#-------------------------------- tri selection -------------------------------
#------------------------------------------------------------------------------

def tri_select(l):
    comparaison = 0
    affectation = 0
    
    for i in range(len(l)):
        indice = i
        min = l[i]
        for j in range(i+1,len(l)):
            comparaison+=1
            if l[j]<min:
                
                min = l[j]
                indice = j
        
        affectation+=1
        l[indice] = l[i]
        l[i] = min
    return (comparaison,affectation)
    
    
    
#------------------------------------------------------------------------------
#-------------------------------- tri insertion -------------------------------
#------------------------------------------------------------------------------    

    
def tri_inser(l):

    comparaison = 0
    affectation = 0

    for i in range(1,len(l)):
        tmp=l[i]
        j=i
        
        while j>0 and tmp<l[j-1]:
            comparaison+=1
            affectation+=1
            l[j]=l[j-1]
            j-=1
        comparaison+=1
        l[j]=tmp
    return (comparaison,affectation)
 
 
 
#------------------------------------------------------------------------------
#-------------------------------- tri shell -----------------------------------
#------------------------------------------------------------------------------
 
def shift_left(lst, index, gap):
    val = lst[index]
    comparaison = 0 
    affectation=0
    
    while index > 0 and lst[index-gap] > val:
        comparaison +=1
        affectation+=1
        lst[index] = lst[index-gap]
        index -= gap
    lst[index] = val
    return comparaison,affectation
    
def shell_sort(lst):
    
    comparaison = 0
    affectation=0
    n = len(lst)
    if n <= 1: 
        return
    
    # calcul du pas initial
    k = floor(log(2*n+1, 3))
    h = (3**k-1)//2
    
    while h > 0:
        # h-tri
        for i in range(h, len(lst)):
            c,a=shift_left(lst, i, h)
            comparaison += c
            affectation += a
            
            
        # passage au pas immédiatement inférieur
        h //= 3
    return comparaison,affectation


#------------------------------------------------------------------------------
#-------------------------------- tri fusion ----------------------------------
#------------------------------------------------------------------------------


def fusion(t1,t2):
    
    i1,i2,n1,n2=0,0,len(t1),len(t2)
    t=[] # listes résultat
    
    #tant qu'aucunes des listes n'est vide
    while i1<n1 and i2<n2:
        # on ajoute l'élément le plus petit entre les deux liste dans t
        if t1[i1]<t2[i2]:
            t.append(t1[i1])
            i1+=1
        else:
            t.append(t2[i2])
            i2+=1
    # si une des listes a été entièrement parcouru, on ajoute l'autre à la fin de t
    if i1==n1:
        t.extend(t2[i2:])
    else:
        t.extend(t1[i1:])
        
    return t
        

# fonction de tri fusion 

def tri_fusion(t):
    #si la liste est plus petite que 2, on renvoie la liste
    if len(t)<2:
        return t
      
    # sinon on rappel tri_fusion sur 2 listes qui sont les 2 moitiés de t
    # et on appelle la fonction fusion sur ces 2 sous-listes de t
    else:
        m=len(t)//2
        return fusion(tri_fusion(t[:m]),tri_fusion(t[m:]))
        
    
#------------------------------------------------------------------------------
#-------------------------------- tri rapide ----------------------------------
#------------------------------------------------------------------------------
     
def tri_rapide(tableau):
    if not tableau:
        return []
    else:
        pivot = tableau[-1]
        plus_petit = [x for x in tableau     if x <  pivot]
        plus_grand = [x for x in tableau[:-1] if x >= pivot]
        return tri_rapide(plus_petit) + [pivot] + tri_rapide(plus_grand)



#------------------------------------------------------------------------------
#-------------------------------- tri rapide ----------------------------------
#------------------------------------------------------------------------------
 
def heapsort( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = length // 2
  for i in range ( leastParent, -1, -1 ):
    moveDown( aList, i, length )

  # flatten heap into sorted array
  for i in range ( length, 0, -1 ):
    if aList[0] > aList[i]:
      swap( aList, 0, i )
      moveDown( aList, 0, i - 1 )

def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      largest += 1

    # right child is larger than parent
    if aList[largest] > aList[first]:
      swap( aList, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return # force exit

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp




#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def test_inplace_sort(f, nb, size):
    print("Sorting", nb, "lists of size", size, "with", f.__name__, ":")
    try:
        for i in range(nb):
            if i % (nb // 20) == 0:
                print("+", end='')
            lst = list(range(size))
            lst2 = lst[:]
            shuffle(lst2)
            lst3 = lst2[:]
            f(lst2)
            assert(lst == lst2)
    except AssertionError as e:
        print("\nError while sorting", lst3, ":")
        print("got", lst2, "")
    else:
        print('\nDone sorting.')



def res_comp_ou_affect_ou_temps(m,pas,mode, liste_fonctions):
    
    
    for f in liste_fonctions:
        
        liste_res = list()
        
        for k in range (2,m,pas):
            lst = list(range(k))
            shuffle(lst)
            if ((mode == 0 or mode ==1) and ( f in [tri_select,tri_inser,shell_sort])):
                liste_res.append(f(lst)[mode])
            elif mode == 2:
                t0=time.time()
                f(lst)
                t = time.time()-t0
                liste_res.append(t)
         
        stri=""
        if "tri_select" in str(f):
            stri=" Tri selection"
        elif "tri_inser" in str(f):
            stri=" Tri insertion"
        elif "shell_sort" in str(f):
            stri=" Tri shell"
        elif "tri_fusion" in str(f):
            stri=" Tri fusion"
        elif "heapsort" in str(f):
            stri=" Tri par tas"
        else:
            stri = " Tri rapide"
        
        if mode == 2 :
            plt.plot(range(2,m,pas), liste_res, linewidth=2.5, linestyle="-", label=stri)
        elif ((mode == 0 or mode ==1) and ( f in [tri_select,tri_inser,shell_sort])):
            plt.plot(range(2,m,pas), liste_res, linewidth=2.5, linestyle="-", label=stri)
        

def comparaison (m,pas,mode,liste_f):
    r= range(2,m,pas)
    res_comp_ou_affect_ou_temps(m,pas,mode,liste_f)
    
    plt.legend(loc='upper left', frameon=False)
    plt.show()
    

#-----------------------------------------------------------------------------
    
fonctions = [tri_fusion,tri_rapide,heapsort]

comparaison(10000,10,2,fonctions)




