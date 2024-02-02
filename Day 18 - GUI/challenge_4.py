from turtle import *
from random import *

tim = Turtle()
tim.pensize(15)
screen = Screen()
screen.colormode(255)
tim.speed("fastest")

for i in range(5000):
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.forward(30)
    tim.setheading(choice([0, 90, 180, 270]))

screen.exitonclick()
