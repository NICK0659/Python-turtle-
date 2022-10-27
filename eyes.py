import turtle as t

t.bgcolor("black")
def draw_eye():
    t.color("white")
    t.right(60)
    t.color("white")
    t.circle(80,120)
    t.left(60)
    t.circle(80,120)
    t.color("black")
    t.right(240)
    t.forward(30)
    t.color("white")
    t.right(90)
    t.circle(40)    
    t.right(90)

draw_eye()
t.color("black")
t.forward(150)
draw_eye()
t.done()
