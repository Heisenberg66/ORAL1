#fréquence d'apparition des printable char ASCII ( 32 à 126)
# 95 caractère

import random
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
# renvoie un liste de tous les caractères ASCII printable
def all_ascii():
    l = list()
    for i in range(32,127):
        l.append(chr(i))
    return l

#------------------------------------------------------------------------------

# renvoie un test de n caractères aléatoires
def random_text(n):
    s=""
    for _ in range(n):
        i = random.randint(32,126)
        s+=chr(i)
    return s

#------------------------------------------------------------------------------

# nombre d'occurence des caractères
def frequence_apparition(chaine,tab):
    for c in chaine:
        if ord(c)-32 > 0 and ord(c)-32<95:
            tab[ord(c)-32]+=1

#------------------------------------------------------------------------------

# ouverture ficher
file = open('voyage_au_centre_de_la_terre.txt', 'r')
#txt to str
text = file.read()

#chaine contenant les printable ascii
all = all_ascii()

#random texte de n caractère
n=10000
s=random_text(n)

#tableau de fréquence
frequence = [0]*95

# 
frequence_apparition(text,frequence)

print(str(len(text)-sum(frequence))+" caractères ne figurant pas dans la tableau ASCII printable (espace compris).")

#transformation occurence en fréquence 
lst2 = list(map(lambda x : x/sum(frequence),frequence))

#isolation des fréquences et des char des lettres seulement
lettres = lst2[33:59]+lst2[65:91]
char_lettre = all[33:59]+all[65:91]


#affichage de tous les ASCII
plt.figure(1)
plt.bar(range(95),lst2)
plt.xlabel('Caractères')
plt.ylabel('Fréquence')
plt.title("Fréquence d'apparition des caractarères ASCII")
plt.xticks(range(95),all)

#affichage des lettres
plt.figure(2)
plt.bar(range(52),lettres)
plt.xlabel('Caractères')
plt.ylabel('Fréquence')
plt.title("Fréquence d'apparition des caractarères ASCII")
plt.xticks(range(52),char_lettre)

plt.show()