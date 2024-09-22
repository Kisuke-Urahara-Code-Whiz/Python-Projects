import time
import turtle
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
bmw = CarManager()
sb = Scoreboard()

screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.right, "Right")
screen.onkey(tim.left, "Left")

i = 0
o = 10

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if i%o==0:
        bmw.create()
    bmw.loco()
    i+=1

    if tim.ycor()>280:
        tim.goto(player.STARTING_POSITION)
        bmw.reset()
        sb.upd()

    if 







turtle.mainloop()