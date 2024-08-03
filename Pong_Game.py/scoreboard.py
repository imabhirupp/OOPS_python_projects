from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    # Setting the scoreboard coordinates and updating the scoreboard after each round
    def update_scoreboard(self):
        self.goto(-100, 250)  # Player A score coordinates
        self.write(f"Player A = {self.l_score}", False, "center", ("Courier", 15, "normal"))
        self.goto(100, 250)  # Player B score coordinates
        self.write(f"Player B = {self.r_score}", False, "center", ("Courier", 15, "normal"))

    # GAME OVER PROMPT
    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Arial", 20, "normal"))

    # counting left paddle player score
    def l_scoreboard(self):
        self.l_score += 1
        self.clear()  # clear the stored value before i.e. clearing the stored score value
        self.update_scoreboard()

    # counting right paddle player score
    def r_scoreboard(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
