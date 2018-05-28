import matplotlib.pyplot as plt
import numpy as np


a=3
b=2
c=1
d=1
interdit = -d/c

x=np.linspace(-4,4,8000)
y=[]

for i in x:
    if i!= interdit:
        y.append((a*i+b)/(b*i+d))
    
    
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x,y,"b.")
axe=plt.gca()
axe.set_ylim([-6,6]) #limite de l'axe des ordonnées
plt.grid()
plt.axes()

plt.show()