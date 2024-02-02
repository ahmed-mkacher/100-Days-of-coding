from turtle import *

tim = Turtle()
screen = Screen()


def turn_right():
    tim.speed("fastest")
    tim.setheading(0)
    tim.forward(20)


def turn_left():
    tim.speed("fastest")
    tim.setheading(180)
    tim.forward(20)


def move_down():
    tim.speed("fastest")
    tim.setheading(270)
    tim.forward(20)


def move_up():
    tim.speed("fastest")
    tim.setheading(90)
    tim.forward(20)


def erase():
    resetscreen()


screen.listen()
screen.onkey(key="z", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="q", fun=turn_left)
screen.onkey(key="space", fun=tim.penup)
screen.onkey(key="v", fun=tim.pendown)
screen.onkey(key="c", fun=erase)
screen.exitonclick()
