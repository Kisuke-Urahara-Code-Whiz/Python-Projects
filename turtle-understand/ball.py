from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")

    def move(self):
        self.fd(5)

    def bouncewall(self):
        a=self.heading()
        if a<=90 and a>=0:
            a=360-a
        elif a<=270 and a>=180:
            a=180-(270-a)
        else:
            a=a+90
            if a>=360:
                a=a-360
        self.setheading(a)


