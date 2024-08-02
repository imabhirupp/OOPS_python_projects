import turtle
import random
from turtle import Turtle

class Food(Turtle):               # inheriting Turtle super class into Food sub-class
    # defining the food features
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)         # creating the size of the food-shape
        self.color("blue")
        self.speed("fastest")

    # defining the random movement of the food
    def refresh(self):
        rand_x = random.randint(-280, 280)                   # creating a random x axis point within the used screen size for the food
        rand_y = random.randint(-280, 280)                   # creating a random y axis point within the used screen size for the food
        self.goto(rand_x, rand_y)                               # randomly sending the food to different axis according to the rules of the snake game


