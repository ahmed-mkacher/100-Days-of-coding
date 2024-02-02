from turtle import *
from random import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randrange(-260, 260, 20)
        random_y = randrange(-260, 260, 20)
        self.goto(random_x, random_y)

