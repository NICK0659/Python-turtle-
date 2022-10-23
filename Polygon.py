import turtle as t 
import time
print("enter the number of sides")
n=int(input())
t.bgcolor("black")
t.title("My First Graphic")
t.speed(1)
t.color("white")
poly_=t.Turtle()
for i in range(n):
    poly_.color("white")
    poly_.forward(100)
    poly_.left(360/n)
t.done()
