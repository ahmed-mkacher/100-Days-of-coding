from turtle import *

POSITIONS = [(0, -285), (-290, 0), (285, 0), (-200, 290), (200, 290)]
SIZE = 40


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.walls = []

    def create_walls(self):
        for pos in POSITIONS:
            self.add_wall(pos)

    def add_wall(self, position):
        new_wall = Turtle("square")
        if position[0] == 0:
            new_wall.shapesize(1, 30)
        elif position[1] == 0:
            new_wall.shapesize(30, 1)
        else:
            new_wall.shapesize(1, 12)
        new_wall.color("white")
        new_wall.speed("fastest")
        new_wall.penup()
        new_wall.goto(position)
        self.walls.append(new_wall)
