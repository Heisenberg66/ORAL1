import random as random

nb = random.randint(1,50)
i=51
print("J'ai choisi un nombre entre 1 et 50 inclus, devine le !")
while i!=nb:
    i = int(input("Ecris un nombre : \n"))
    if i>nb:
        print("C'est moins")
    elif i<nb:
        print("C'est plus")
print("Bravo tu as trouver, le nombre était bien :"+str(i))