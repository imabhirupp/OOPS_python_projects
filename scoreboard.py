import turtle
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()       # calling the scoreboard feature in order to display the score value in screen

    # defining the score features
    def update_scoreboard(self):
        self.write(f"Score {self.score}", False, "center", ("Arial", 15, "normal"))

    def game_over(self):
        self.color("white")
        self.goto(0,0)
        self.write(f"GAME OVER", False, "center", ("Arial", 20, "normal"))

    # counting the score
    def count(self):
        self.score += 1
        self.clear()                            # clear the stored value before i.e. clearing the stored score value
        self.update_scoreboard()

    # creating game over for when the snake hits the wall
