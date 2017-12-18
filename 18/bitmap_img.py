# importation des librairies

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random as rd


def rand_img(l,c):
    b = 1 * np.ones((l, l, 4), dtype=np.uint16)
    
    for i in range(l):
        
        for j in range(c):
            
            for k in range(3):
                
                r = rd.randint(0,255)
                b[i,j,k]=r
    
    return b
    
    
    


def inverser(img):
    
    b=img.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):

            pixel = b[i,j] # récupération du pixel

            # on calcule le complement à MAX pour chaque composante - effet négatif
            p = (1 - pixel[0], 1 - pixel[1], 1 - pixel[2],1)

            # composition de la nouvelle image
            
            b[i,j]=p
    return b
        

def retourne (matrice):
    b = matrice.copy()
    l = len(b)
   
    i=0
    while i<l//2:
        b[i],b[l-1-i] = b[l-1-i].copy(),b[i].copy()
        i+=1
    return b
    
def retourne2 (matrice):
    b = matrice.copy()
   
    i=0
    while i<b.shape[1]//2:
        b[:,i],b[:,b.shape[1]-1-i] = b[:,b.shape[1]-1-i].copy(),b[:,i].copy()
        i+=1
    return b           


def fusionne(img01,img02):
    
    b=img01.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):

            pixel1 = img01[i,j] # récupération du pixel
            pixel2 = img02[i,j]
            p =(min(pixel1[0],pixel2[0]),min(pixel1[1],pixel2[1]),min(pixel1[2],pixel2[2]),1 )

            # composition de la nouvelle image
            
            b[i,j]=p
    return b

def niveau_de_gris(img):
    b=img.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):

            pixel = (int(255 * (1-img[i,j,0])),int(255 * (1-img[i,j,1])),int(255 * (1-img[i,j,2])))
            gris = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
            
            p=(gris,gris,gris,1)
                                
            b[i,j]=p
            
   
    return b
    
    
def niveau_de_gris2(img):
    b=img.copy()
    
    for i in range(b.shape[0]):

        for j in range(b.shape[1]):

            pixel = (int(255 * (1-img[i,j,0])),int(255 * (1-img[i,j,1])),int(255 * (1-img[i,j,2])))
            gris = int(0.33 * pixel[0] + 0.33 * pixel[1] + 0.33 * pixel[2])
            
            p=(gris,gris,gris,1)
                                
            b[i,j]=p
            
   
    return b
    
    
def filtrage(img,mode):
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
            
   
    return b


def noir_et_blanc(img):
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
            
   
    return b

def histogrammes (img):
    r = [0]*256
    v = [0]*256
    b = [0]*256
    
    for i in range(img.shape[0]):

        for j in range(img.shape[1]):
            
            r[int(255 * (1-img[i,j,0]))]+=1
            v[int(255 * (1-img[i,j,1]))]+=1
            b[int(255 * (1-img[i,j,2]))]+=1
    
    return r,v,b
    


# ouverture du fichier image

ImageFileTWD = "/Users/Boulanger/Documents/COURS/M1/Oral 1/18/tiger.png"
ImageFileGOT = "/Users/Boulanger/Documents/COURS/M1/Oral 1/18/got.png"
ImageFileCS = "/Users/Boulanger/Documents/COURS/M1/Oral 1/18/chapelle_sixtine.png"


img1=mpimg.imread(ImageFileGOT)
img2=mpimg.imread(ImageFileTWD)
img3=mpimg.imread(ImageFileCS)

random_image=rand_img(600,600)

r,v,b = histogrammes(img3)

plt.figure(200)
plt.imshow(img3)
plt.axis('off')

plt.figure(1)
plt.subplot(311)
plt.plot(range(256),r,'r-')

plt.subplot(312)
plt.plot(range(256),v,'g-')

plt.subplot(313)
plt.plot(range(256),b,'b-')
plt.show()


# 
# plt.figure(300)
# plt.imshow(inverser(img3))
# plt.axis('off')
# 
# plt.figure(400)
# plt.imshow(retourne(img3))
# plt.axis('off')
# 
# plt.figure(500)
# plt.imshow(retourne2(img3))
# plt.axis('off')
# 
# plt.figure(600)
# plt.imshow(niveau_de_gris(img3))
# plt.axis('off')
# 
# plt.figure(700)
# plt.imshow(fusionne(img1,img1))
# plt.axis('off')
# 
# plt.figure(800)
# plt.imshow(filtrage(img3,'V'))
# plt.axis('off')
# 
# plt.figure(900)
# plt.imshow(noir_et_blanc(img3))
# plt.axis('off')
# 
# plt.show()

