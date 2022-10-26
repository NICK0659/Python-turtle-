import turtle as t
import time
t.bgcolor("yellow")
star=t.Turtle()
for i in range(50):
    star.color("red")
    star.speed(20)
    star.circle(90,120)
    star.forward(100)
    star.left(50)
t.done()