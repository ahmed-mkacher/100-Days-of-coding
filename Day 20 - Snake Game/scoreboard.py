from turtle import *

FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(0, 267)
        self.write(f"Score:{self.score}", False, ALIGN, FONT)

    def game_over(self):
        self.goto(0, 50)
        self.write(f"Game over", False, ALIGN, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_start(self):
        self.goto(0, 0)
        self.write(f'Press "Space" to play the game', False, ALIGN, FONT)
        self.goto(0, -40)
        self.write(f'Press "Escape" to quit', False, ALIGN, FONT)
