from turtle import *
from random import *

tim = Turtle()
tim.hideturtle()
screen = Screen()
screen.colormode(255)

colors = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85),
          (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53),
          (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159),
          (212, 183, 177), (176, 198, 203), (150, 115, 120)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(10):
    for j in range(10):
        tim.dot(20, choice(colors))
        if j < 9:
            tim.forward(50)
    if i % 2 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
    else:
        tim.right(90)
        tim.forward(50)
        tim.right(90)

screen.exitonclick()
