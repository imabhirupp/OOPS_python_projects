from turtle import Turtle


class Paddle(Turtle):
    # Creating and defining the paddle shape, size and position
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(4, 1, 0)
        self.color("white")
        self.goto(position)

    # Creating the Up movement of the paddle
    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    # Creating the Down movement of the paddle
    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)


