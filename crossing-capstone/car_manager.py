from turtle import Turtle
from random import randint,choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.y = []
        self.move = STARTING_MOVE_DISTANCE
        for i in range(-280,280,20):
            self.y.append(i)
        self.use = []
        self.usec = []
        self.chan = 6

    def create(self):
        for i in range(0,randint(0,self.chan)):
            self.car = Turtle()
            self.car.shape("square")
            self.car.shapesize(stretch_len=2,stretch_wid=1)
            self.car.color(choice(COLORS))
            self.car.penup()
            a = choice(self.y)
            for j in self.usec:
                if a==j:
                    continue
            self.usec.append(a)
            self.car.goto(280, a )
            self.cars.append(self.car)

    def loco(self):
        for i in range(0,len(self.cars)):
            self.cars[i].bk(self.move)

    def reset(self):
        self.chan-=1
        self.move+=MOVE_INCREMENT
















