from turtle import *
from random import *

tim = Turtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)
tim.pensize(2)

angle = 0
for i in range(181):
    tim.circle(150)
    tim.setheading(angle)
    angle += 2
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))

screen.exitonclick()
