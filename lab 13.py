#victoria dynak
#victoria.dynak61@login.cuny.edu
#september 20,2022
#this program creates a brown turtle that navigates in the shape of a triangle
#while leaving a stamp at each corner.

import turtle
victoria = turtle.Turtle()
victoria.shape("turtle")
victoria.color("#964B00")
n=3
for x in range(n):
    victoria.forward(100)
    victoria.left(360/n)
    victoria.stamp()
