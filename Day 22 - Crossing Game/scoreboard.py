from turtle import *

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(-210, 245)
        self.write(f"Level:{self.level}", False, "center", FONT)

    def level_increase(self):
        self.clear()
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", ("Arial", 30, "bold"))
