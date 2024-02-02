from turtle import *
from random import *

height = -175
screen = Screen()
screen.colormode(255)
screen.setup(width=900, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

finish_line = Turtle()
racers = []
colors = ["red", "green", "blue", "yellow", "black", "purple"]
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(410, -150)

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    racers.append(new_turtle)

for racer in racers:
    racer.penup()
    racer.speed("fast")
    height += 50
    racer.goto(-410, height)

finish_line.pendown()
finish_line.left(90)
finish_line.forward(315)

win = False

while not win:
    for racer in racers:
        racer.forward(randint(1, 10))
        place = racer.pos()
        if place[0] >= 410:
            win = True
            winner = racer.pencolor()

if winner == user_bet:
    print("You won!")
else:
    print("You lost")
print(f"The winner is {winner}")
screen.exitonclick()

