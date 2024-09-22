FONT = ("Courier", 15, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200,260)
        self.level = 1
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def upd(self):
        self.clear()
        self.level+=1
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

