#victoria dynak
#victoria.dynak61@login.cuny.edu
#september 25 2022
#cyan shades

import turtle
victoria = turtle.Turtle()
turtle.colormode(255)
victoria.penup()
victoria.backward(100)
victoria.left(90)
victoria.backward(100)
victoria.right(90)
victoria.pendown()

for i in range(0,255,10):
    victoria.forward(10)
    victoria.pensize(i)
    victoria.color(0,i,i)


dynak = turtle.Turtle()

dynak.penup()
dynak.backward(100)
dynak.left(90)
dynak.backward(100)
dynak.right(0)
dynak.pendown()

for x in range(0,255,10):
    dynak.forward(10)
    dynak.pensize(x)
    dynak.color(0,x,x)
