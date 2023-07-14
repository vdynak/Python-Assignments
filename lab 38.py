#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 6 2022
#draw shape functions

import turtle
import math
t = turtle.Turtle()

def drawPantegon(t, length, numEdges):
    if numEdges > 0:
        t.forward(length)
        t.left(72)
        drawPantegon(t,length,numEdges-1)
def cornerPantegon(t, length):
    if length>= 25:
        drawPantegon(t, length, 5)
        updatedlength = length//2
        length = updatedlength
        cornerPantegon(t,length)
def nestedPantegon(t,length):
    if length >= 25:
        drawPantegon(t,length,5)
        t.forward(length/2)
        t.left(36)
        nestedPantegon(t,length*math.sin(54/180*math.pi))
