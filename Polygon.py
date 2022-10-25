import turtle as t 
import time
print("enter the number of sides")
n=int(input())
t.bgcolor("yellow")
t.title("My First Graphic")
t.speed(1)
poly_=t.Turtle()
for i in range(n):
    poly_.shape("turtle")
    poly_.color("red","yellow")
    poly_.forward(100)
    poly_.left(360/n)
t.done()
