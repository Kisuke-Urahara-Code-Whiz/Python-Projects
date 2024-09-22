# from turtle import Turtle, Screen
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("red","green")
# timmy.fd(100)
#
#
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
# table.add_column("Type",["Electric","Water","Fire"])
# table.align='l'
# print(table.align)
# print(table)
#
#import turtle as t #aliasing t. .....
from turtle import Turtle, Screen
timmy=Turtle()
timmy.shape("turtle")
timmy.color("firebrick1")
#pencolor(), fillcolor(r,g,b) and tkinter module(GUI module)turtle is dependent on for its GUI
timmy.speed("fastest")
for i in range(72):
    timmy.circle(50)
    ch=timmy.heading()
    print (ch)
    timmy.setheading(ch+5)

# colours=["magenta","cyan2","goldenrod","MediumSpringGreen","MediumTurquoise","magenta4","red1","black"]
# import random
# timmy.pensize(10)
# dic={
#       1: timmy.fd,
#       2: timmy.right,
#       3: timmy.left,
#       4: timmy.bk
# }
# for i in range(200):
#     timmy.color(colours[random.randint(0,7)])
#     a=random.randint(1,4)
#     if a==1 or a==4:
#         c=dic[a]
#         c(20)
#     else:
#         c=dic[a]
#         c(90)
#         timmy.fd(20)


# def shapes(l1,l2):
#     i=0
#     for j in range(l1,l2+1):
#         timmy.color(colours[i])
#         angle=360/j
#         for a in range(j):
#             timmy.fd(100)
#             timmy.right(angle)
#         i=i+1
# shapes(3,10)


#square
# for i in range(0,4):
#     timmy.fd(100)
#     timmy.right(90)

#dashed line
# for i in range(25):
#     timmy.fd(5)
#     timmy.penup()
#     timmy.fd(5)
#     timmy.pendown()

#triangle
# timmy.fd(100)
# timmy.left(120)
# timmy.fd(100)
# timmy.left(120)
# timmy.fd(100)

#pentagon
# for i in range(5):
#     timmy.fd(100)
#     timmy.right(72)

#hexagon
# for i in range(6):
#     timmy.fd(100)
#     timmy.right(60)

#heptagon
# for i in range(7):
#     timmy.fd(100)
#     timmy.right(360/7)

#octagon
# for i in range(8):
#     timmy.fd(100)
#     timmy.right(360/8)

#nonagon
# for i in range(9):
#     timmy.fd(100)
#     timmy.right(40)

#decagon
# for i in range(10):
#     timmy.fd(100)
#     timmy.right(36)

#setheading(0,90,180,360) - another way of turning through angles
#random.choice(list)
#pencolor(r,g,b) - 255 each - tuple
#tuple is like list but brackets tuple=(, , , ) same index just it's immutable unlike list
#list is a type like dictionary and it can be returned too



screen = Screen()
screen.exitonclick()



