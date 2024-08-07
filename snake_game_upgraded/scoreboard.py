import turtle
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt", mode="r") as file:     # reading the highscore from the high_score.txt at the begining of the game
            self.highscore = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()       # calling the scoreboard feature in order to display the score value in screen

    # defining the score features
    def update_scoreboard(self):
        self.clear()                    # clear the stored value before i.e. clearing the stored score value
        self.write(f"Score {self.score} High Score {self.highscore}", False, "center", ("Arial", 15, "normal"))

    # Resetting the game to achieve high score
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
            self.update_scoreboard()
            with open("high_score.txt", mode="w") as file:        # writing the highscore in high_score.txt after each time the game resets
                file.write(f"{self.highscore}")

    # counting the score
    def count(self):
        self.score += 1
        self.update_scoreboard()

