from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    # Turtle features
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto_start()
        self.setheading(90)

    # Turtle Starting Position
    def goto_start(self):
        self.goto(STARTING_POSITION)

    # Move the turtle upward with key
    def up(self):
        self.forward(MOVE_DISTANCE)

    # Check if reached finish line
    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
