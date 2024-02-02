from paddle import *
from ball import *
from time import *
from scoreboard import *

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

pad_1 = Paddle((-380, 0))
pad_2 = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.score()

screen.listen()

screen.onkey(pad_1.go_up, "7")
screen.onkey(pad_1.go_down, "4")
screen.onkey(pad_2.go_up, "8")
screen.onkey(pad_2.go_down, "5")

game = True

while game:
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    if (ball.distance(pad_2) < 80 and ball.xcor() >= 350) or (ball.distance(pad_1) < 80 and ball.xcor() <= -350):
        ball.bounce()
        ball.reverse()
    if ball.xcor() >= 390:
        ball.restart()
        scoreboard.p1_increase()
    elif ball.xcor() <= -390:
        ball.restart()
        scoreboard.p2_increase()
screen.exitonclick()
