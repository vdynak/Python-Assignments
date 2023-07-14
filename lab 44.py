#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 13 2022
#flowers

import turtle

def petal(color, angle):
    turtle.colormode(255)
    victoria = turtle.Turtle(visible=False)
    victoria.shape("turtle")
    victoria.left(angle)
    for x in range(0,255,10):
        victoria.forward(10)
        victoria.pensize(x)
        if color == "red":
            victoria.pencolor(x,0,0)
        elif color == "green":
            victoria.pencolor(0,x,0)
        elif color == "blue":
            victoria.pencolor(0,0,x)
        elif color == "yellow":
            victoria.pencolor(x,x,0)
        elif color == "purple":
            victoria.pencolor(x,0,x)
        elif color == "cyan":
            victoria.pencolor(0,x,x)
        else:
            victoria.pencolor(0,x,0)
    victoria.pensize(0)

def flower(color,num):
    for x in range(num):
        petal(color,x*360/num)

def main():
    flower("green",9)

if __name__ == "__main__":
    main()
