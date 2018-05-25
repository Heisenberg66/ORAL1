 
# == Presentation du modele Lokta-Volterra ==
# Source : https://fr.wikipedia.org/wiki/%C3%89quations_de_pr%C3%A9dation_de_Lotka-Volterra
#		   http://scipy-cookbook.readthedocs.io/items/LoktaVolterraTutorial.html
# 
# ======================================================================================
# Le Lokta-volterra model plus connu sous le nom des équations proie-predateur
# Ces équations différentielles sont utilisés pour décrire le système biologique
# dans lequel 2 éspèces interargissent, une étant la proie et l'autre le prédateur. 
#
# du/dt =  a*u -   b*u*v
# dv/dt = -c*v + d*b*u*v 
# 
# Avec :
# 
# *  u : Nombre de proie (Des lapins par exemple)
# 
# *  v : Nombre de prédateur(Des renards par exemple)  
#   
# * a, b, c, d sont des constantes diffinissant le comportement des deux populations :    
# 
#   + a est le taux de reproduction intrinsèque des proies (constant, indépendant du nombre de prédateurs)
# 
#   + b taux de mortalité des proies dû aux prédateurs rencontrés
# 
#   + c taux de mortalité intrinsèque des prédateurs (constant, indépendant du nombre de proies)
# 
#   + d taux de reproduction des prédateurs en fonction des proies rencontrées et mangées 
# 
# 

# Nous utiliserons X=[u,v] pour décrire l'état des population au cours du temps
# 

from numpy import *
from scipy import integrate
import matplotlib.pyplot as p

# Parametres
a = 1.
b = 0.1
c = 1.5
d = 0.75

def dX_dt(X, t=0):
    """ Renvoie les taux de croissance des lapins et des renards"""
    return array([ a*X[0] -   b*X[0]*X[1] ,  
                  -c*X[1] + b*d*X[0]*X[1] ])

t = linspace(0, 15,  1000)              # temps (1000 valeurs)
X0 = array([10, 5])                     # conditions initiales: 10 lapins and 5 renards  

#https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.integrate.odeint.html
#
# dX_dt : fonction de dérivation au temps dt
# X0 : valeurs initiales
# t : sequence de valeurs représentant le temps 
X = integrate.odeint(dX_dt, X0, t)


lapins, renards = X.T

f1 = p.figure()
p.plot(t, lapins, 'r-', label='Lapins')
p.plot(t, renards  , 'b-', label='Renards')
p.legend(loc=1)
p.grid()
p.xlabel('temps')
p.ylabel('Population')
p.title('Evolution des populations de lapins et de renards')
p.show()
