from turtle import *
from random import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
old_y = 0


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = MOVE_INCREMENT

    def create_car(self):
        random_chance = randint(1, 6)
        global old_y
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.speed("fastest")
            new_car.color(choice(COLORS))
            random_y = randint(-240, 240)
            while old_y == random_y:
                random_y = randint(-240, 240)
            old_y = random_y
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def cars_restart(self):
        self.clear()
        self.move_speed *= 1.1
