from time import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import *

screen = Screen()
game_speed = 0.1
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
wall = Wall()
wall.create_walls()

game = True


# def change():
#     global game
#     game = True


# scoreboard.game_start()

screen.listen()
screen.onkey(snake.up, "z")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "q")
# screen.onkeypress(change, "a")

while game:
    screen.update()
    sleep(game_speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        game_speed *= 0.999
        scoreboard.increase_score()

    if snake.head.xcor() >= 278 or snake.head.xcor() <= -278 or snake.head.ycor() >= 278 or snake.head.ycor() <= -278:
        scoreboard.game_over()
        game = False

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 15:
            game = False
            scoreboard.game_over()


screen.exitonclick()
mainloop()
