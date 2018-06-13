import random as random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
# c*(b-a)

            
def disque_biaise(n):
    list_x = list()
    list_y = list()
    
    for _ in range(0,n):
        x= random.uniform(-1,1)
        y= random.uniform(-1,1)
        while x**2+y**2>=1:
            y= random.uniform(-1,1)
        list_x.append(x)
        list_y.append(y)
    
    return list_x,list_y
    
def disque_uniforme(n):
    list_x = list()
    list_y = list()
    

    for _ in range(0,n):
        x= random.uniform(-1,1)
        y= random.uniform(-1,1)
        if x**2+y**2<1:
            list_x.append(x)
            list_y.append(y)
    return list_x,list_y
    
    
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
    
    
    return list_x,list_y,pi
    
    

x,y = disque_biaise(10000)
x1,y1 = disque_uniforme(10000)
x2,y2,leg = monte_carlo(10000)

plt.figure()
plt.plot(x,y,'b.')
plt.figure()
plt.plot(x1,y1,'b.')
plt.figure()
plt.plot(x2,y2,'b.',label=leg)
plt.legend(loc=1)
plt.show()