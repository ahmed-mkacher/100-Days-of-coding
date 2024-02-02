from turtle import *
from random import *

tim = Turtle()
screen = Screen()

def draw_shape(sides):
    for i in range(sides):
        tim.forward(100)
        tim.right(360 / sides)


screen.colormode(255)

for j in range(3, 11):
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    draw_shape(j)

screen.exitonclick()