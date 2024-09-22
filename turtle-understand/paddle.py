from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,a,b):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(a,b)

    def up(self):
        if self.ycor()<250:
            self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        if self.ycor()>-250:
            self.goto(self.xcor(), self.ycor()-20)
