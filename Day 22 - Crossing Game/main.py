import time
from turtle import Screen
from player import Player
from cars import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars_gen = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.035)
    screen.update()
    cars_gen.create_car()
    cars_gen.move_cars()

    # Detect collision with car
    for car in cars_gen.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.player_restart()
        cars_gen.cars_restart()
        scoreboard.level_increase()

screen.exitonclick()

