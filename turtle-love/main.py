from turtle import Turtle, Screen

a = Turtle()
b = Screen()
a.speed(10)
b.setup(width=500, height=500)
a.pencolor("red")
a.penup()
a.goto(0, -125)
a.pendown()
a.setheading(45)
a.fd(200)
c=45
while(c!=225):
    c=c+5
    a.setheading(c)
    a.fd(5)
print(a.pos())
a.fd(56.91)
a.setheading(135)
a.fd(56.91)
d=135
while(d!=315):
    d=d+5
    a.setheading(d)
    a.fd(5)
print(a.pos())
a.fd(173.20)
print(a.pos())

b.exitonclick()
