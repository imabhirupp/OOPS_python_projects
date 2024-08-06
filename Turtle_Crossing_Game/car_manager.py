from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []                                        # list of all cars
        self.car_speed = MOVE_INCREMENT

    # Creating and defining the features of the car
    def create(self):
        chances = random.randint(1,6)
        if chances == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)                          # adding each car after creating to the all_cars list

    # Moving the call at random speed
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Leveling up by increasing the speed each time the turtle reaches the finish line
    def level_up(self):
        self.car_speed += 5

