import tkinter as Tk
from turtle import *

def Haut(e):
    if heading()!=90:
        seth(90)
    forward(1)
 
def Bas(e):
    if heading()!=270:
        seth(270)
    forward(1)
 
def Droite(event):
    if heading()!=0:
        seth(0)
    forward(1)
    
def Gauche(event):
    if heading()!=180:
        seth(180)
    forward(1)
 
fenetre = Tk.Tk()
fenetre.bind('<Up>', Haut)
fenetre.bind('<Down>', Bas)
fenetre.bind('<Right>', Droite)
fenetre.bind('<Left>', Gauche)
fenetre.mainloop()