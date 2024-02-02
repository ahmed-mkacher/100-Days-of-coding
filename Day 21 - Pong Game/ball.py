from turtle import *
from random import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.x_speed = 10
        self.y_speed = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_speed *= -1

    def reverse(self):
        self.y_speed = randrange(10, 20)
        self.x_speed *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_speed *= -1
