import matplotlib.pyplot as plt
import numpy as np


def retourne (matrice):
    b = matrice.copy()
    l = len(matrice)
   
    i=0
    while i<len(b)//2:
        b[i],b[l-1-i] = b[l-1-i].copy(),b[i].copy()
        i+=1
    return b
    
def retourne2 (matrice):
    b = matrice.copy()
    l = len(matrice)
   
    i=0
    while i<len(b)//2:
        b[:,i],b[:,l-1-i] = b[:,l-1-i].copy(),b[:,i].copy()
        i+=1
    return b

def symetrie_centrale(matrice):
    b = matrice.copy()
    l = len(matrice)
   
    i=0
    while i<len(b)//2:
        b[i],b[l-1-i] = b[l-1-i].copy()[::-1],b[i].copy()[::-1]
        i+=1
    return b





# matrice 32*32*3, 32*32 = size et le 3 =  RVB
a = 255 * np.ones((32, 32, 3), dtype=np.uint16)

# pour l'instant, tous les pixels de la matrice 32*32 sont blancs (255,255,255)

#lignes noires
a[10] = 0    #la ligne 10 sont des pixels noirs
a[23] = 0
a[:, 5] = 0  #toute les ligne de la colonne 5 sont en noire
a[:, 26] = 0
a[:18, 14] = 0 # colonne 14, les ligne du début à 18
a[17, :14] = 0 #ligne 17 , colonne du début à 14



# rectangle de la ligne 11 à 17 et de la colonne 6:14 en rouge 
a[11:17,6:14]= (255,0,0)
# a[11:17, 6:14, 1:] = 0


#rectangle en bleu
a[24:, 6:26]=(0,0,255)


#rectangle en vert
a[:10, 27:] = (0,255,0)

b=rotate(a,45)




plt.figure(200)
plt.imshow(a)
plt.axis('off')

plt.figure(300)
plt.imshow(b)
plt.axis('off')

plt.show()

