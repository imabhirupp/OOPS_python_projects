from turtle import Turtle

FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):

    # Defining the Level
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-290, 270)
        self.track_score()

    # Updating the level
    def track_score(self):
        self.clear()
        self.write(f"Level = {self.level}", align="Left", font=FONT)

    # Increasing the level
    def increase_level(self):
        self.level += 1
        self.track_score()

    # GAME OVER
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="Center", font=("Arial", 20, "bold"))
