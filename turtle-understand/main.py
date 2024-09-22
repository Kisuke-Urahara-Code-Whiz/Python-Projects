from turtle import Turtle, Screen
from paddle import Paddle
from random import randint
from ball import Ball
import time

sc = Screen()
sc.tracer(0)
sc.bgcolor("black")
sc.setup(800, 600)
sc.title("Pong Game")

b = Ball()

start = sc.textinput(title="Game start choice", prompt="Who starts the game? l  or r and specify 1 or 2?")
if start=="l1":
    b.setheading(randint(115,180))
elif start=="l2":
    b.setheading(randint(180,245))
elif start=="r1":
    b.setheading(randint(0,65))
else:
    b.setheading(randint(295,360))




l = Paddle(-390,0)
r = Paddle(390, 0)

sc.listen()
sc.onkey(l.up, "w")
sc.onkey(r.up, "Up")
sc.onkey(l.down, "s")
sc.onkey(r.down, "Down")

game = True

while game:
    time.sleep(0.03)
    sc.update()
    b.move()

    if b.ycor()>289 or b.ycor()<-289:
        b.bouncewall()

    if l.distance(b)<=50:
        if b.ycor()<=l.ycor()+50 and b.ycor()>l.ycor()+30:
            if b.heading()<=180 and b.heading()>=90:
                b.setheading(90-(180-b.heading()))
            else:
                b.setheading(b.heading()+180)

    if r.distance(b)<=50:
        if b.ycor()<=r.ycor()+50 and b.ycor()>r.ycor()+30:
            if b.heading()<=90 and b.heading()>=0:
                b.setheading(180-b.heading())
            else:
                b.setheading(b.heading()+180)

















sc.exitonclick()