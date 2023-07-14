#victoria dynak
#victoria.dynak61@login.cuny.edu
#september 25 2022
#cyan shades

import turtle
victoria = turtle.Turtle()
turtle.colormode(255)
victoria.penup()
victoria.backward(300)
victoria.left(90)
victoria.backward(100)
victoria.right(90)
victoria.pendown()

for x in range(0,255,10):
    victoria.forward(10)
    victoria.pensize(x)
    victoria.color(x,0,x)

for i in range(255,0,-10):
    victoria.forward(10)
    victoria.pensize(i)
    victoria.color(i,0,i)


