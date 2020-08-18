import turtle
a = turtle.Turtle()
a.shape("turtle")
a.penup()
size = 20
for i in range(30):
    a.stamp()
    size=size+3
    a.forward(size)
    a.right(30)
turtle.done()