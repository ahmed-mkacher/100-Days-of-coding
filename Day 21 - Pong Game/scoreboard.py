from turtle import *

FONT = ("Courier", 200, "bold")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.hideturtle()
        self.penup()
        self.color("grey")
        self.speed("fastest")

    def score(self):
        self.goto(-200, -150)
        self.write(self.p1_score, False, ALIGN, FONT)
        self.goto(200, -150)
        self.write(self.p2_score, False, ALIGN, FONT)

    def p1_increase(self):
        self.clear()
        self.p1_score += 1
        self.score()

    def p2_increase(self):
        self.clear()
        self.p2_score += 1
        self.score()
