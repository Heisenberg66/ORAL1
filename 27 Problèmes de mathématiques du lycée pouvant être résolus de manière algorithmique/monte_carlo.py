import random as random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
# c*(b-a)

def monte_carlo(n):
    list_x = list()
    list_y = list()
    

    for _ in range(0,n):
        x= random.random()
        y= random.random()
        if x**2+y**2<1:
            list_x.append(x)
            list_y.append(y)
    
    pi = (len(list_x)/n)
    pi= " p = "+str(pi)+" "
    
    plt.plot(list_x,list_y,'b.',label=pi)
    plt.legend(loc=1)
    plt.show()
            
            
def cinq(n):
    list_x = list()
    list_y = list()
    

    for _ in range(0,n):
        x= random.uniform(0,1)
        y= random.uniform(0,1)
        while abs(x-y)<=0.5:
            y= random.uniform(0,1)
        list_x.append(x)
        list_y.append(y)
    
    pi = (len(list_x)/n)
    pi= " p = "+str(pi)+" "
    
    plt.plot(list_x,list_y,'b.',label=pi)
    plt.legend(loc=1)
    plt.show()
    
    
#monte_carlo(10000)
cinq(10000)