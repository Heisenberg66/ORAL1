from turtle import *
import random

#active les contrôle
def keys_activate():
    listen()
    onclick(changecolor) #click sur la turtle
    onscreenclick(pencilv) #click screen
    onkey(hexagone,"n")
    onkey(carre,"v")
    onkey(triangle,"b")
    onkey(pentagone,"c")
    onkeypress(appui_sur_up, "Up")
    onkeypress(appui_sur_down, "Down")
    onkeypress(appui_sur_right, "Right")
    onkeypress(appui_sur_left, "Left")
    ondrag(goto)
    penup()
    
#désactive les contrôle
def keys_deactivate():
    onscreenclick(None)
    onkey(None,"n")
    onkey(None,"v")
    onkey(None,"b")
    onkey(None,"c")
    onkeypress(None, "Up")
    onkeypress(None, "Down")
    onkeypress(None, "Right")
    onkeypress(None, "Left")
    ondrag(None)

#déplacements de la turtle
def appui_sur_up():
    if heading()!=90:
        seth(90)
    forward(3)    
def appui_sur_down():
    if heading()!=270:
        seth(270)
    forward(3)    
def appui_sur_right():
    if heading()!=0:
        seth(0)
    forward(3)    
def appui_sur_left():
    if heading()!=180:
        seth(180)
    forward(3)
    
# dessin figures
def pentagone():
    keys_deactivate()
    pendown()
    for _ in range(5):
        for _ in range(30):
            fd(1)
        right(72)
    keys_activate()

def hexagone():
    keys_deactivate()
    pendown()
    for _ in range(6):
        for _ in range(30):
            fd(1)
        right(60)
    keys_activate()

def carre():
    keys_deactivate()
    pendown()
    for _ in range(4):
        for _ in range(40):
            fd(1)
        right(90)
    keys_activate()


def triangle():
    keys_deactivate()
    pendown()
    for _ in range(3):
        for _ in range(40):
            fd(1)
        right(120)
    keys_activate()



# méthodes couleur et crayon
def pencilv(x,y):
    if isdown():
        penup()        
    else:
        pendown()
        
def changecolor(x,y):
    r = lambda: random.randint(0,255)
    c = color("#%06x" % random.randint(0, 0xFFFFFF))
    color(c,c)
    pendown()
    
# setup    
    
title("Welcome to the turtle!")

speed(0)

keys_activate()

mainloop()