#victoria.dynak61@login.cuny.edu
#victoria dynak
#9/5/22

import turtle
t=turtle.Turtle()
t.pensize(5)
t.shape("circle")


for x in ["green", "blue", "cyan","red"]:
    t.color(x)
    t.forward(300)
    for y in range(2):
        t.right(90)
        t.forward(100)
    t.right(90)
