#name: victoria dynak
#email: victoria.dynak61@login.cuny.edu
import turtle
t = turtle.Turtle() #create a turtle object called t
#t.forward(100)
#t.left(90)
#t.forward(100)
#t.left(90)
#t.forward(100)
#t.left(90)
#t.forward(100)
#t.left(90)
#turtle.Screen().exitonclick()
n = 12
for i in range(n):
    t.forward(50)
    t.left(360/n)

turtle.Screen().exitonclick()



