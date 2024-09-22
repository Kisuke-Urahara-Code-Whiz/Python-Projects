import colorgram
import turtle
import random

colors = colorgram.extract("download.jpg", 30)
colours = []

for i in colors:
    r = i.rgb.r
    b = i.rgb.b
    g = i.rgb.g
    new_color = (r,g,b)
    colours.append(new_color)
    # colours.append(i.rgb)
    #hsl

turtle.colormode(255)
sc= turtle.Screen()
sc.setup(width=500, height=500)
tim = turtle.Turtle()
tim.penup()
tim.goto(x=-125 , y=-125)
# tim.dot(10, random.choice(colours))
i1=0
for i in range(15):

    for i in range(15):
        tim.dot(10, random.choice(colours))
        tim.fd(15)

    i1+=1
    if i1%2==0:
        tim.setheading(90)
        tim.fd(15)
        tim.setheading(360)
    else:
        tim.setheading(90)
        tim.fd(15)
        tim.setheading(180)




sc.exitonclick()