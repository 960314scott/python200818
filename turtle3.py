import turtle
i=0
a = turtle.Turtle()
a.shape("turtle")
b = turtle.Turtle()
b.shape("turtle")
a.color("gold")
b.color("blue")
a.pensize(5)
b.pensize(5)
for i in range(360):
    a.forward(1)
    a.left(1)
    b.forward(1)
    b.right(1)
turtle.done()