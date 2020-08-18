import turtle

i=1
a = turtle.Turtle()
b=turtle.Screen()
a.shape("turtle")
a.color("gold")
b.bgcolor("pink")
while i<360:
    a.forward(1)
    a.left(1)
    i=i+1
i=1
p=1
while i<3600:
    a.left(p)
    a.forward(2)
  
    p=p+0.1
turtle.done()
