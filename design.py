# code to print star pattern using turtle
import turtle as t 
import time
def particlestyle():
    print("enter the number of sides")
    n=int(input())
    t.bgcolor("black")
    t.title("My First Graphic")
    star=t.Turtle()
    for i in range(n):
        star.color("white")
        star.forward(300)
        star.left(130)
    t.done()

particlestyle()