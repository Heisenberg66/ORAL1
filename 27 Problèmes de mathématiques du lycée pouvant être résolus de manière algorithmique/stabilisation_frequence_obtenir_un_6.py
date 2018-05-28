import random as random
import matplotlib.pyplot as plt


def tirage (k):
    obtient_un_6 =0
    for _ in range(k):
       r = random.randint(1,6)
       if r == 6:
           obtient_un_6+=1
    return obtient_un_6/k
    

def stabilisation (n):
    liste =[]
    for i in range(1,n):
        liste.append(tirage(i))
    print(sum(liste)/len(liste))
    plt.plot(range(1,n),liste,'-.')
    plt.show()
    
stabilisation(1000)
     
           
