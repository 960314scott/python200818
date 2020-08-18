import turtle
a = turtle.Turtle()
ans=int(input("請輸入邊數"))
for i in range(ans):
    a.forward(100)
    a.left(180-(((ans-2)*180)/ans))

turtle.done()