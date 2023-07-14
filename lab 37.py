#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 6 2022
#flower recusion

import turtle
t = turtle.Turtle()

def flowerRecursion(t,n):
    if n>0:
        t.forward(100)
        t.left(105)
        t.forward(52)
        t.left(105)
        t.forward(100)
        t.right(170)
        flowerRecursion(t,n-1)

def main():
    if __name__ == "__main__":
        main()
