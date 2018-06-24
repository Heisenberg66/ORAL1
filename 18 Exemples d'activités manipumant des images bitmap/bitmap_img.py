# importation des librairies

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random as rd
import time

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#génère une image avec des pixels de couleur aléatoire

def rand_img(l,c):
    print("rand_img : En cours")
    
    b = 1.0 * np.ones((l, l, 4), dtype=np.uint16)
    
    for i in range(l):
        
        for j in range(c):
            
            for k in range(3):
                
                r = rd.random()
                b[i,j,k]=float(r)
    print(b)
    plt.figure(2)
    plt.imshow(b)
    plt.axis('off')
    
    return b
    
#-------------------------------------------------------------------------------

# renvoie le négatif de l'image 

def inverser(img):
    print("inverser : En cours")
    
    b=img.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):

            pixel = b[i,j] # récupération du pixel

            # on calcule le complement à 1 pour chaque composante - effet négatif
            p = (1 - pixel[0], 1 - pixel[1], 1 - pixel[2],1)
            
            b[i,j]=p
    return b
    
    plt.figure(3)
    plt.imshow(b)
    plt.axis('off')
        

#-------------------------------------------------------------------------------


# symétrie par l'axe vertical central

def retourne (matrice):
    
    print("retourne : En cours")
    
    b = matrice.copy()
    l = len(b)
   
    i=0
    while i<l//2:
        b[i],b[l-1-i] = b[l-1-i].copy(),b[i].copy()
        i+=1
    
    
    plt.figure(4)
    plt.imshow(b)
    plt.axis('off')
   
#-------------------------------------------------------------------------------
   
# symétrie par l'axe horizontal
    
def retourne2 (matrice):
    
    print("Retourne2 : En cours")
    
    b = matrice.copy()
   
    i=0
    while i<b.shape[1]//2:
        b[:,i],b[:,b.shape[1]-1-i] = b[:,b.shape[1]-1-i].copy(),b[:,i].copy()
        i+=1
    plt.figure(5)
    plt.imshow(b)
    plt.axis('off')           

#-------------------------------------------------------------------------------

#symétrie par rapport à l'axe diagonale

def symetrie_centrale(matrice):
    
    print("symetrie_centrale : En cours")
    
    b = matrice.copy()
    l = len(matrice)
   
    i=0
    while i<len(b)//2:
        b[i],b[l-1-i] = b[l-1-i].copy()[::-1],b[i].copy()[::-1]
        i+=1
    plt.figure(6)
    plt.imshow(b)
    plt.axis('off')
    
#-------------------------------------------------------------------------------

# fusionne deux images

def fusionne(img01,img02):
    
    print("fusionne : En cours")
    
    b=img01.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):

            pixel1 = img01[i,j] # récupération du pixel
            pixel2 = img02[i,j]
            p =(min(pixel1[0],pixel2[0]),min(pixel1[1],pixel2[1]),min(pixel1[2],pixel2[2]),1 )

            # composition de la nouvelle image
            
            b[i,j]=p
    plt.figure(7)
    plt.imshow(b)
    plt.axis('off')

#-------------------------------------------------------------------------------

# transformation RBG en niveau de gris

def niveau_de_gris(img):
    
    print("niveau_de_gris : En cours")
    
    b=img.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):

            pixel = (int(255 * (1-img[i,j,0])),int(255 * (1-img[i,j,1])),int(255 * (1-img[i,j,2])))
            gris = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
            
            p=(gris,gris,gris)
                                
            b[i,j]=p
            
    plt.figure(8)
    plt.imshow(b)
    plt.axis('off')
    
    return b

#-------------------------------------------------------------------------------

# autre formule du niveau de gris
    
def niveau_de_gris2(img):
    
    print("niveau_de_gris2 : En cours")
    
    b=img.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):

            pixel = (int(255 * (1-img[i,j,0])),int(255 * (1-img[i,j,1])),int(255 * (1-img[i,j,2])))
            gris = int(0.33 * pixel[0] + 0.33 * pixel[1] + 0.33 * pixel[2])
            
            p=(gris,gris,gris,1)
                                
            b[i,j]=p
            
   
    plt.figure(9)
    plt.imshow(b)
    plt.axis('off')
 
#-------------------------------------------------------------------------------
   
# selectionne le canal en argument (R,V ou B)
    
def filtrage(img,mode):
    
    print("filtrage : En cours")

    b=img.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):
            
            pixel= img[i,j]
            
            if mode == 'R':
                p=(pixel[1],0,0,1)
                
            elif mode == 'V':
                p=(0,pixel[1],0,1)
                
            elif mode == 'B':
                p=(0,0,pixel[2],1)
                                
            b[i,j]=p
            
   
    plt.figure(10)
    plt.imshow(b)
    plt.axis('off')

#-------------------------------------------------------------------------------

# conversion en niveau de gris puis en noir et blanc

def noir_et_blanc(img):
    
    print("noir_et_blanc : En cours")

    
    b=img.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):

            pixel = (int(255 * (1-img[i,j,0])),int(255 * (1-img[i,j,1])),int(255 * (1-img[i,j,2])))
            gris = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
            p=(gris,gris,gris,1)
            pixel = p
            
            if pixel[0]>=128:
                p=1
            else:
                p=0
            
            
                                
            b[i,j]=(p,p,p,1)
            
    plt.figure(11)
    plt.imshow(b)
    plt.axis('off')

#-------------------------------------------------------------------------------

# histogramme R V B

def histogrammes (img):
    
    print("histogrammes : En cours")

    
    r = [0]*256
    v = [0]*256
    b = [0]*256
    
    for i in range(img.shape[0]):

        for j in range(img.shape[1]):
            
            r[int(255 * (1-img[i,j,0]))]+=1
            v[int(255 * (1-img[i,j,1]))]+=1
            b[int(255 * (1-img[i,j,2]))]+=1
    
    plt.figure(1)
    plt.subplot(311)
    plt.plot(range(256),r,'r-')

    plt.subplot(312)
    plt.plot(range(256),v,'g-')

    plt.subplot(313)
    plt.plot(range(256),b,'b-')

#-------------------------------------------------------------------------------
    
# extrait une image rectangle venant de l'original 
# (x1,y1) -> top left corner
# (x2,y2) -> bottom right corner
    
def extraction (img,x1,y1,x2,y2):
    
    print("extraction : En cours")

    
    if x1<img.shape[0] and x2<img.shape[0] and y1<img.shape[1] and y2<img.shape[1] and x1<x2 and y1<y2:
        
        plt.figure(12)
        plt.imshow(img[x1:x2,y1:y2,:])
        plt.axis('off')
        
    

#-------------------------------------------------------------------------------
    
# renforce les couleurs  
# argument : liste [a,b,g] avec a,b,g flottant entre [0,1]  
    
def renforcement_couleur(img,liste):
    
    print("renforcement_couleur : En cours")

    
    b=img.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):
            
            if b[i,j,0]+liste[0]<=1:
                b[i,j,0]+=liste[0]
            else:
                b[i,j,0]=1
            if b[i,j,1]+liste[1]<=1:
                b[i,j,1]+=liste[1]
            else:
                b[i,j,1]=1
            if b[i,j,2]+liste[2]<=1:
                b[i,j,2]+=liste[2]
            else:
                b[i,j,2]=1
    
    plt.figure(13)
    plt.imshow(b)
    plt.axis('off')
    
#-------------------------------------------------------------------------------
    
def filtre (img,f33):
    
    b = img.copy()
    s = sum(sum(f33))
    print(s)
    if s==0:
        s=1
    
    for i in range(1,b.shape[0]-1):

         for j in range(1,b.shape[1]-1):
            
            for k in range(3):
                
                b[i,j,k] = (b[i-1,j-1,k]*f33[0,0]+b[i-1,j,k]*f33[0,1]+b[i-1,j+1,k]*f33[0,2]+
                            b[i,j-1,k]*f33[1,0]+b[i,j+1,k]*f33[1,2]+b[i+1,j-1,k]*f33[2,0]+
                                b[i+1,j,k]*f33[2,1]+b[i+1,j+1,k]*f33[2,2]+b[i,j,k]*f33[1,1])/s
                
    
    plt.figure(14)
    plt.imshow(b)
    plt.axis('off')    
    
#------------------------------------------------------------------------------
    
    
def filtre2 (img,f33):
    
    b = niveau_de_gris(img)
    copie = b.copy()

    s = sum(sum(f33))
    if s==0:
        s=1

    for i in range(1,b.shape[0]-1):

         for j in range(1,b.shape[1]-1):
             
                    
            p1 = b[i-1,j-1,0]*f33[0,0]
            p2 = b[i-1,j,0]*f33[0,1]
            p3 = b[i-1,j+1,0]*f33[0,2]
            p4 = b[i,j-1,0]*f33[1,0]
            p5 = b[i,j,0]*f33[1,1]
            p6 = b[i,j+1,0]*f33[1,2]
            p7 = b[i+1,j-1,0]*f33[2,0]
            p8 = b[i+1,j,0]*f33[2,1]
            p9 = b[i+1,j+1,0]*f33[2,2]
            
            
            
            tmp = p1+p2+p3+p4+p5+p6+p7+p8+p9
            tmp=tmp/s
            
            
            # if tmp < 0: tmp = 0
            # if tmp > 255: tmp = 255
            tmp+=128
            tmp = 255-tmp
            copie[i,j]=(tmp,tmp,tmp)
          
                
    
    plt.figure(14)
    plt.imshow(copie)
    plt.axis('off')  

#-------------------------------------------------------------------------------  

def steganographie (img1,img2):
    print("steganographie : En cours")

    
    b=img1.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):
            
            
            b[i,j,0]= round(b[i,j,0],3)+(img2[i,j,0]/1000)
            b[i,j,1]= round(b[i,j,1],3)+(img2[i,j,1]/1000)
            b[i,j,2]= round(b[i,j,2],3)+(img2[i,j,2]/1000)
            
    return b
    # plt.figure(15)
    # plt.imshow(b)
    # plt.axis('off') 

#-------------------------------------------------------------------------------  

def recup(img):
    
    print("recup : En cours")

    b = img.copy()
    
    for i in range(img.shape[0]):

        for j in range(img.shape[1]):
            
            b[i,j,0]= (b[i,j,0]*1000) - int(b[i,j,0]*1000)
            b[i,j,1]= (b[i,j,1]*1000) - int(b[i,j,1]*1000) 
            b[i,j,2]= (b[i,j,2]*1000) - int(b[i,j,2]*1000)
            
    plt.figure(16)
    plt.imshow(b)
    plt.axis('off')


            
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
    
    
ImageFileTWD = "tiger.png"
ImageFileGOT = "got.png"
ImageFileCS = "chapelle_sixtine.png"
ImageFileBB = "big_ben.png"


# ouverture du fichier image

img1=mpimg.imread(ImageFileGOT)
img2=mpimg.imread(ImageFileTWD)
img3=mpimg.imread(ImageFileCS)
img4=mpimg.imread(ImageFileBB)

RGB_renforcement=[0.2,0,0]
filtre_3x3 = np.ones((3,3))
f = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])


plt.figure(200)
plt.imshow(img3)
plt.axis('off')

#r_image = rand_img(600,600)
# 
# inverser(img3)
# 
# retourne(img3)
# 
# retourne2(img3)
# 
# symetrie_centrale(img3)
# 
# fusionne(img1,img2)
# 
# niveau_de_gris(img3)
# 
# niveau_de_gris2(img3)
# 
# filtrage(img3,'R')
# 
# noir_et_blanc(img3)
# 
# histogrammes(img1)
# 
# extraction(img3,500,500,700,700)
# 
renforcement_couleur(img3,RGB_renforcement)

# filtre2(img4,f)

#recup(steganographie(img1,img2))


plt.show()

